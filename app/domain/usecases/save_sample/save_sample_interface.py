from abc import ABC, abstractmethod

from domain.entities.sample import Sample
from domain.utils.response import Response


class SaveSampleUseCaseInterface(ABC):
    @abstractmethod
    async def save(self, sample: Sample) -> Response[Sample]:
        pass
