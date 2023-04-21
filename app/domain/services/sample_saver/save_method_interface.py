from abc import ABC, abstractmethod

from app.domain.entities.sample import Sample
from app.domain.utils.response import Response


class SaveMethodInterface(ABC):
    @abstractmethod
    def save(self, sample: Sample) -> Response[Sample]:
        pass
