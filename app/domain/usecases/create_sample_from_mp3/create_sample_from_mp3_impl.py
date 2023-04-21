from app.domain.entities.mp3_file import Mp3File
from app.domain.entities.sample import Sample
from app.domain.services.create_sample_service.create_sample_service_interface import CreateSampleServiceInterface
from app.domain.utils.response import Response
from app.domain.usecases.create_sample_from_mp3.create_sample_from_mp3_interface import (
    CreateSampleFromMp3UseCaseInterface,
)
from app.domain.usecases.mp3_file.mp3_file_interface import Mp3FileUseCaseInterface


class CreateSampleFromMp3UseCase(CreateSampleFromMp3UseCaseInterface):
    def __init__(
        self, mp3_file_usecase: Mp3FileUseCaseInterface, create_sample_service: CreateSampleServiceInterface
    ) -> None:
        self.mp3_file_usecase = mp3_file_usecase
        self.create_sample_service = create_sample_service

    async def execute(self, upload_mp3_file: Mp3File, minutes_per_sample: int) -> Response[Sample]:
        mp3_file_response = await self.mp3_file_usecase.execute(upload_mp3_file.name, upload_mp3_file.path)

        if not mp3_file_response.success:
            return Response(success=False, body=mp3_file_response.body)

        sample_response = await self.create_sample_service.execute(
            mp3_file=mp3_file_response.body, minutes_per_sample=minutes_per_sample
        )

        if not sample_response.success:
            return Response(success=False, body=sample_response.body)

        return Response(success=True, body=sample_response.body)
