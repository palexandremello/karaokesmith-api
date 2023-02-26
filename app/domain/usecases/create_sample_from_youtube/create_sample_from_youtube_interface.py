from abc import ABC, abstractmethod
from domain.entities.sample import Sample

from domain.utils.response import Response


class CreateSampleFromYoutubeUseCaseInterface(ABC):
    @abstractmethod
    async def execute(self, video_url: str) -> Response[Sample]:
        pass
