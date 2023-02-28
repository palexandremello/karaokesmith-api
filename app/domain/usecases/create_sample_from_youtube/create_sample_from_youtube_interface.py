from abc import ABC, abstractmethod
from domain.entities.sample import Sample

from domain.utils.response import Response


class CreateSampleFromYoutubeUseCaseInterface(ABC):
    @abstractmethod
    async def execute(self, video_url: str, minutes_per_sample: int) -> Response[Sample]:
        pass
