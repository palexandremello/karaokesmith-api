from abc import ABC, abstractmethod

from domain.entities.sample import Sample
from domain.utils.response import Response


class SaveMethodInterface(ABC):
    @abstractmethod
    def save(self, sample: Sample) -> Response[Sample]:
        pass
