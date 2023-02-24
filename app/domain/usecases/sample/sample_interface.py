from abc import ABC, abstractmethod
from typing import Optional

from domain.entities.sample import Sample


class SampleUseCase(ABC):
    @abstractmethod
    async def execute(
        self, name: Optional[str], minutes_per_sample: int, video_url: Optional[str], upload_mp3_file: Optional[str]
    ) -> Sample:
        pass
