from abc import ABC, abstractmethod
from typing import List

from app.domain.entities.sample import Sample
from app.domain.utils.response import Response
from app.domain.entities.mp3_file import Mp3File


class SampleSaverInterface(ABC):
    @abstractmethod
    def save_sample(self, sample: Sample) -> Response[List[Mp3File]]:
        pass
