from abc import ABC, abstractmethod

from domain.entities.sample import Sample
from domain.utils.response import Response


class SampleSaverInterface(ABC):
    @abstractmethod
    async def save_sample(self, sample: Sample) -> Response:
        pass
