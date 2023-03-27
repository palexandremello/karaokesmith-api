from abc import ABC, abstractmethod
from typing import Optional
from domain.entities.sample import Sample
from domain.utils.response import Response


class SampleRepositoryInterface(ABC):
    @abstractmethod
    async def save(self, sample: Sample) -> Response[Sample]:
        pass

    @abstractmethod
    async def get(self, sample_id: str) -> Response[Optional[Sample]]:
        pass

    @abstractmethod
    async def delete(self, sample_id: str) -> Response:
        pass
