from abc import ABC, abstractmethod

from app.domain.entities.mp3_file import Mp3File
from app.domain.entities.sample import Sample
from app.domain.utils.response import Response


class CreateSampleFromMp3UseCaseInterface(ABC):
    @abstractmethod
    async def execute(self, upload_mp3_file: Mp3File, minutes_per_sample: int) -> Response[Sample]:
        pass
