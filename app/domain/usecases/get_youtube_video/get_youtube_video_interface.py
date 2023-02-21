from abc import ABC, abstractmethod
from domain.entities.video_source import VideoSource

from domain.utils.response import Response


class GetYoutubeVideoUseCaseInterface(ABC):

    @abstractmethod
    async def get(self, video_url: str) -> Response[VideoSource]:
        pass