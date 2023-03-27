from domain.entities.sample import Sample
from domain.services.sample_saver.sample_saver_interface import SampleSaverInterface
from domain.repositories.sample_repository_interface import SampleRepositoryInterface
from domain.utils.response import Response
from .save_sample_interface import SaveSampleUseCaseInterface


class SaveSampleUseCase(SaveSampleUseCaseInterface):
    def __init__(self, repository: SampleRepositoryInterface, sample_saver: SampleSaverInterface) -> None:
        self.repository = repository
        self.sample_saver = sample_saver

    async def save(self, sample: Sample) -> Response[Sample]:
        response = await self.sample_saver.save_sample(sample=sample)

        if not response.success:
            return Response(success=False, body=response.body)

        response = await self.repository.save(sample=response.body)

        if not response.success:
            return Response(success=False, body=response.body)

        return response
