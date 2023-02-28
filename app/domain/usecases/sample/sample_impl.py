from typing import Optional
from domain.entities.sample import Sample
from domain.usecases.create_sample_from_mp3.create_sample_from_mp3_interface import CreateSampleFromMp3UseCaseInterface
from domain.usecases.create_sample_from_youtube.create_sample_from_youtube_interface import (
    CreateSampleFromYoutubeUseCaseInterface,
)
from domain.usecases.sample.sample_interface import SampleUseCaseInterface
from domain.utils.response import Response


class SampleUseCase(SampleUseCaseInterface):
    def __init__(
        self,
        create_sample_from_youtube_usecase: CreateSampleFromYoutubeUseCaseInterface,
        create_sample_from_mp3_usecase: CreateSampleFromMp3UseCaseInterface,
    ) -> None:
        self.create_sample_from_youtube_usecase = create_sample_from_youtube_usecase
        self.create_sample_from_mp3_usecase = create_sample_from_mp3_usecase

    async def execute(
        self,
        minutes_per_sample: int,
        name: Optional[str] = None,
        video_url: Optional[str] = None,
        upload_mp3_file: Optional[str] = None,
    ) -> Response[Sample]:
        if upload_mp3_file:
            sample_response = await self.create_sample_from_mp3_usecase.execute(upload_mp3_file, minutes_per_sample)

        else:
            sample_response = await self.create_sample_from_youtube_usecase.execute(video_url)

        if not sample_response.success:
            return Response(success=False, body=sample_response.body)

        return Response(success=True, body=sample_response.body)
