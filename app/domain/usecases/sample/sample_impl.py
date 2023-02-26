from typing import Optional
from domain.entities.sample import Sample
from domain.services.create_sample_service.create_sample_service_interface import CreateSampleServiceInterface
from domain.usecases.mp3_file.mp3_file_interface import Mp3FileUseCaseInterface
from domain.usecases.sample.sample_interface import SampleUseCaseInterface
from domain.usecases.youtube_audio.youtube_audio_interface import YoutubeAudioUseCaseInterface
from domain.utils.response import Response


class SampleUseCase(SampleUseCaseInterface):
    def __init__(
        self,
        youtube_audio_usecase: YoutubeAudioUseCaseInterface,
        mp3_file_usecase: Mp3FileUseCaseInterface,
        create_sample_service: CreateSampleServiceInterface,
    ) -> None:
        self.youtube_audio_usecase = youtube_audio_usecase
        self.mp3_file_usecase = mp3_file_usecase
        self.create_sample_service = create_sample_service

    async def execute(
        self, name: Optional[str], minutes_per_sample: int, video_url: Optional[str], upload_mp3_file: Optional[str]
    ) -> Response[Sample]:
        if upload_mp3_file:
            pass

        else:
            youtube_audio_response = await self.youtube_audio_usecase.execute(video_url)
            if not youtube_audio_response.success:
                return youtube_audio_response

        sample_response = await self.create_sample_service.execute(youtube_audio_response.body.mp3_file)

        if not sample_response.success:
            return Response(success=False, body=sample_response.body)

        return Response(success=True, body=sample_response.body)
