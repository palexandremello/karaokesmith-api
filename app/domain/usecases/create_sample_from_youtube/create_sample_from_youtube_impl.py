from app.domain.entities.sample import Sample
from app.domain.services.create_sample_service.create_sample_service_interface import CreateSampleServiceInterface
from app.domain.usecases.create_sample_from_youtube.create_sample_from_youtube_interface import (
    CreateSampleFromYoutubeUseCaseInterface,
)
from app.domain.usecases.youtube_audio.youtube_audio_interface import YoutubeAudioUseCaseInterface
from app.domain.utils.response import Response


class CreateSampleFromYoutubeUseCase(CreateSampleFromYoutubeUseCaseInterface):
    def __init__(
        self,
        youtube_audio_usecase: YoutubeAudioUseCaseInterface,
        create_sample_service: CreateSampleServiceInterface,
    ) -> None:
        self.youtube_audio_usecase = youtube_audio_usecase
        self.create_sample_service = create_sample_service

    async def execute(self, video_url: str, minutes_per_sample: int) -> Response[Sample]:
        youtube_audio_response = await self.youtube_audio_usecase.execute(video_url)

        if not youtube_audio_response.success:
            return Response(success=False, body=youtube_audio_response.body)

        sample_response = self.create_sample_service.execute(youtube_audio_response.body.mp3_file, minutes_per_sample)

        if not sample_response.success:
            return Response(success=False, body=sample_response.body)

        return Response(success=True, body=sample_response.body)
