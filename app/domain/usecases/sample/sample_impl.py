from typing import Optional
from domain.entities.sample import Sample
from domain.services.create_sample_service.create_sample_service_interface import CreateSampleServiceInterface
from domain.usecases.get_youtube_video.get_youtube_video_interface import GetYoutubeVideoUseCaseInterface
from domain.usecases.mp3_file.mp3_file_interface import Mp3FileUseCaseInterface
from domain.usecases.sample.sample_interface import SampleUseCaseInterface
from domain.usecases.video_to_audio_converter.video_to_audio_converter_interface import (
    VideoToAudioConverterUseCaseInterface,
)
from domain.usecases.youtube_audio.youtube_audio_interface import YoutubeAudioUseCaseInterface
from domain.utils.response import Response


class SampleUseCase(SampleUseCaseInterface):
    def __init__(
        self,
        get_youtube_video_usecase: GetYoutubeVideoUseCaseInterface,
        video_to_audio_converter_usecase: VideoToAudioConverterUseCaseInterface,
        youtube_audio_usecase: YoutubeAudioUseCaseInterface,
        mp3_file_usecase: Mp3FileUseCaseInterface,
        create_sample_service: CreateSampleServiceInterface,
    ) -> None:
        self.get_youtube_video_usecase = get_youtube_video_usecase
        self.video_to_audio_converter_usecase = video_to_audio_converter_usecase
        self.youtube_audio_usecase = youtube_audio_usecase
        self.mp3_file_usecase = mp3_file_usecase
        self.create_sample_service = create_sample_service

    async def execute(
        self, name: Optional[str], minutes_per_sample: int, video_url: Optional[str], upload_mp3_file: Optional[str]
    ) -> Response[Sample]:
        if upload_mp3_file is None:
            video_response = await self.get_youtube_video_usecase.get(video_url)

            if not video_response.success:
                return video_response

            converted_video_response = await self.video_to_audio_converter_usecase.convert(video_response.body)

            if not converted_video_response.success:
                return converted_video_response

            youtube_audio_response = await self.youtube_audio_usecase.execute(video_url)

            if not youtube_audio_response.success:
                return youtube_audio_response

            sample_response = await self.create_sample_service.execute(youtube_audio_response.body.mp3_file)

        if not sample_response.success:
            return Response(success=False, body=sample_response.body)

        return Response(success=True, body=sample_response.body)
