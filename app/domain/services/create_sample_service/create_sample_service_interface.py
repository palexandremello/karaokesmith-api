from abc import ABC, abstractmethod

from domain.entities.mp3_file import Mp3File
from domain.entities.sample import Sample
from domain.utils.response import Response


class CreateSampleServiceInterface(ABC):
    @abstractmethod
    async def execute(self, mp3_file: Mp3File, minutes_per_sample: int) -> Response[Sample]:
        pass
