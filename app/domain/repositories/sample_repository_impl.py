from domain.entities.sample import Sample
from domain.repositories.sample_repository_interface import SampleRepositoryInterface
from domain.services.sample_saver.sample_saver_interface import SampleSaverInterface
from domain.utils.response import Response


class SampleRepository(SampleRepositoryInterface):
    def __init__(self, sample_saver: SampleSaverInterface,
                 ) -> None:
        self.sample_saver = sample_saver

    def save(self, sample: Sample) -> Response[Sample]:
        pass    