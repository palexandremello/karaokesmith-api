from io import BytesIO
from app.domain.entities.sample import Sample
from app.domain.services.create_sample_service.create_sample_service_interface import CreateSampleServiceInterface
from app.domain.utils.response import Response
from app.domain.usecases.create_sample_from_mp3.create_sample_from_mp3_interface import (
    CreateSampleFromMp3UseCaseInterface,
)
from app.domain.usecases.mp3_file.mp3_file_interface import Mp3FileUseCaseInterface
from app.domain.utils.logger.logger_interface import LoggerInterface


class CreateSampleFromMp3UseCase(CreateSampleFromMp3UseCaseInterface):
    def __init__(
        self,
        mp3_file_usecase: Mp3FileUseCaseInterface,
        create_sample_service: CreateSampleServiceInterface,
        logger: LoggerInterface,
    ) -> None:
        self.mp3_file_usecase = mp3_file_usecase
        self.create_sample_service = create_sample_service
        self.logger = logger

    async def execute(self, name: str, upload_mp3_file: BytesIO, minutes_per_sample: int) -> Response[Sample]:
        self.logger.info("Creating sample from mp3 file")
        mp3_file_response = await self.mp3_file_usecase.execute(name, upload_mp3_file)

        if not mp3_file_response.success:
            self.logger.error(f"{mp3_file_response.body}")
            return Response(success=False, body=mp3_file_response.body)

        sample_response = self.create_sample_service.execute(
            mp3_file=mp3_file_response.body, minutes_per_sample=minutes_per_sample
        )

        if not sample_response.success:
            return Response(success=False, body=sample_response.body)

        return Response(success=True, body=sample_response.body)
