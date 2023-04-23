from abc import ABC, abstractmethod
from typing import List

from app.domain.entities.sample import Sample
from app.domain.utils.response import Response


class SaveMethodInterface(ABC):
    @abstractmethod
    def save(self, samples: List[Sample]) -> Response[List[Sample]]:
        pass
