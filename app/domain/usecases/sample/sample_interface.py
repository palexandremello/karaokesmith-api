from abc import ABC, abstractmethod
from typing import Optional

from domain.entities.sample import Sample
from domain.utils.response import Response


class SampleUseCaseInterface(ABC):
    @abstractmethod
    async def execute(
        self, name: Optional[str], minutes_per_sample: int, video_url: Optional[str], upload_mp3_file: Optional[str]
    ) -> Response[Sample]:
        pass
