from app.application.controllers.create_sample.create_sample_controller import CreateSampleController
from app.domain.usecases.get_youtube_video.get_youtube_video_impl import GetYoutubeVideoUseCase
from app.domain.usecases.sample.sample_impl import SampleUseCase
from app.domain.usecases.create_sample_from_mp3.create_sample_from_mp3_impl import CreateSampleFromMp3UseCase
from app.domain.usecases.mp3_file.mp3_file_impl import Mp3FileUseCase
from app.domain.usecases.save_sample.save_sample_impl import SaveSampleUseCase
from app.domain.usecases.youtube_audio.youtube_audio_impl import YoutubeAudioUseCase
from app.domain.usecases.video_to_audio_converter.video_to_audio_converter_impl import VideoToAudioConverterUseCase
from app.domain.services.mp3_file.mp3_file_service import Mp3FileService
from app.domain.services.youtube_video.youtube_video_service import YoutubeVideoService
from app.domain.services.video_converter.video_converter_service import VideoConverterService
from app.domain.services.create_sample_service.create_sample_service import CreateSampleService
from app.domain.usecases.create_sample_from_youtube.create_sample_from_youtube_impl import (
    CreateSampleFromYoutubeUseCase,
)
from app.infra.gateways.filesystem_mp3_file_validator import FileSystemMp3FileValidator
from app.infra.gateways.sampler.pydub_sampler import PydubSampler
from app.infra.gateways.ytdlp_video_downloader import YtDlpVideoDownloader
from app.infra.repos.mongodb.mongodb_sample_repository import MongoDbSampleRepository
from app.infra.logger.logger import Logger

from pymongo import MongoClient

from app.domain.services.sample_saver.sample_saver import SampleSaver
from app.infra.gateways.save_method.filesystem_save_method import FilesystemSaveMethod
from app.main.config.settings import MONGODB_URI


def create_sample_composer():
    logger = Logger.get_instance()

    mp3_validator = FileSystemMp3FileValidator()
    mp3_file_service = Mp3FileService(validator=mp3_validator)
    mp3_file_usecase = Mp3FileUseCase(mp3_file_service=mp3_file_service)
    pydub_sampler = PydubSampler()
    create_sample_service = CreateSampleService(sampler=pydub_sampler, logger=logger)
    create_sample_from_mp3_usecase = CreateSampleFromMp3UseCase(
        mp3_file_usecase=mp3_file_usecase, create_sample_service=create_sample_service, logger=logger
    )

    youtube_video_downloader = YtDlpVideoDownloader()
    youtube_video_service = YoutubeVideoService(youtube_video_downloader=youtube_video_downloader)
    get_youtube_video_usecase = GetYoutubeVideoUseCase(youtube_video_service=youtube_video_service)

    video_converter_service = VideoConverterService(converter="")
    video_to_audio_converter_usecase = VideoToAudioConverterUseCase(
        video_converter_service=video_converter_service, logger=logger
    )
    youtube_audio_usecase = YoutubeAudioUseCase(
        get_youtube_video_usecase=get_youtube_video_usecase,
        video_to_audio_converter_usecase=video_to_audio_converter_usecase,
    )
    create_sample_from_youtube_usecase = CreateSampleFromYoutubeUseCase(
        youtube_audio_usecase=youtube_audio_usecase, create_sample_service=create_sample_service
    )

    mongodb_repository = MongoDbSampleRepository(
        mongo_client=MongoClient(MONGODB_URI),
        database_name="karaokesmith",
        collection_name="sample",
    )

    save_method_service = FilesystemSaveMethod(logger=logger)
    sample_saver_service = SampleSaver(save_method=save_method_service)
    save_sample_usecase = SaveSampleUseCase(
        repository=mongodb_repository, sample_saver=sample_saver_service, logger=logger
    )
    sample_usecase = SampleUseCase(
        create_sample_from_mp3_usecase=create_sample_from_mp3_usecase,
        create_sample_from_youtube_usecase=create_sample_from_youtube_usecase,
        save_sample_usecase=save_sample_usecase,
        logger=logger,
    )
    create_sample_controller = CreateSampleController(sample_usecase=sample_usecase, logger=logger)

    return create_sample_controller
