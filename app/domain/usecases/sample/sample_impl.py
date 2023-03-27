from typing import Optional
from domain.entities.sample import Sample
from domain.repositories.sample_repository_interface import SampleRepositoryInterface
from domain.usecases.create_sample_from_mp3.create_sample_from_mp3_interface import CreateSampleFromMp3UseCaseInterface
from domain.usecases.create_sample_from_youtube.create_sample_from_youtube_interface import (
    CreateSampleFromYoutubeUseCaseInterface,
)
from domain.usecases.sample.sample_interface import SampleUseCaseInterface
from domain.usecases.save_sample.save_sample_interface import SaveSampleUseCaseInterface
from domain.utils.response import Response


class SampleUseCase(SampleUseCaseInterface):
    def __init__(
        self,
        create_sample_from_youtube_usecase: CreateSampleFromYoutubeUseCaseInterface,
        create_sample_from_mp3_usecase: CreateSampleFromMp3UseCaseInterface,
        save_sample_usecase: SaveSampleUseCaseInterface,
    ) -> None:
        self.create_sample_from_youtube_usecase = create_sample_from_youtube_usecase
        self.create_sample_from_mp3_usecase = create_sample_from_mp3_usecase
        self.save_sample_usecase = save_sample_usecase

    async def execute(
        self,
        minutes_per_sample: int,
        name: Optional[str] = None,
        video_url: Optional[str] = None,
        upload_mp3_file: Optional[str] = None,
    ) -> Response[Sample]:
        if upload_mp3_file:
            sample_response = await self.create_sample_from_mp3_usecase.execute(upload_mp3_file, minutes_per_sample)
            response = await self.save_sample_usecase.save(sample_response.body)

        elif video_url:
            sample_response = await self.create_sample_from_youtube_usecase.execute(video_url, minutes_per_sample)
            response = await self.save_sample_usecase.save(sample_response.body)

        if not response.success:
            return Response(success=False, body=response.body)

        return Response(success=True, body=response.body)
