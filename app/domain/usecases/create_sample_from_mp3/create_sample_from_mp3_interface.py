from abc import ABC, abstractmethod
from io import BytesIO

from app.domain.entities.sample import Sample
from app.domain.utils.response import Response


class CreateSampleFromMp3UseCaseInterface(ABC):
    @abstractmethod
    async def execute(self, name: str, upload_mp3_file: BytesIO, minutes_per_sample: int) -> Response[Sample]:
        pass
