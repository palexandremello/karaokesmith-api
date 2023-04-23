from typing import List
from app.domain.entities.sample import Sample
from app.domain.services.sample_saver.sample_saver_interface import SampleSaverInterface
from app.domain.repositories.sample_repository_interface import SampleRepositoryInterface
from app.domain.utils.response import Response
from app.domain.utils.logger.logger_interface import LoggerInterface
from .save_sample_interface import SaveSampleUseCaseInterface


class SaveSampleUseCase(SaveSampleUseCaseInterface):
    def __init__(
        self, repository: SampleRepositoryInterface, sample_saver: SampleSaverInterface, logger: LoggerInterface
    ) -> None:
        self.repository = repository
        self.sample_saver = sample_saver
        self.logger = logger

    def save(self, samples: List[Sample]) -> Response[Sample]:
        response = self.sample_saver.save_sample(samples=samples)

        if not response.success:
            return Response(success=False, body=response.body)

        response = self.repository.save(samples=response.body)

        if not response.success:
            self.logger.error(f"Error saving samples into repository: {response.body}")
            return Response(success=False, body=response.body)

        return response
