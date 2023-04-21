from abc import ABC, abstractmethod
from typing import Optional

from app.domain.entities.sample import Sample
from app.domain.utils.response import Response


class SampleUseCaseInterface(ABC):
    @abstractmethod
    async def execute(
        self,
        minutes_per_sample: int,
        name: Optional[str] = None,
        video_url: Optional[str] = None,
        upload_mp3_file: Optional[str] = None,
    ) -> Response[Sample]:
        pass
