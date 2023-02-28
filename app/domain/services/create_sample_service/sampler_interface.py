from abc import ABC, abstractmethod
from typing import List

from domain.entities.mp3_file import Mp3File


class SamplerInterface(ABC):
    @abstractmethod
    async def execute(self, mp3_file: Mp3File, minutes_per_sample: int) -> List[Mp3File]:
        pass
