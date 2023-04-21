from abc import ABC, abstractmethod
from app.domain.entities.sample import Sample
from app.domain.utils.response import Response


class CreateSampleFromYoutubeUseCaseInterface(ABC):
    @abstractmethod
    async def execute(self, video_url: str, minutes_per_sample: int) -> Response[Sample]:
        pass
