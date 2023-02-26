from abc import ABC, abstractmethod

from domain.entities.mp3_file import Mp3File
from domain.entities.sample import Sample
from domain.utils.response import Response


class CreateSampleFromMp3UseCaseInterface(ABC):
    @abstractmethod
    async def execute(self, upload_mp3_file: Mp3File) -> Response[Sample]:
        pass
