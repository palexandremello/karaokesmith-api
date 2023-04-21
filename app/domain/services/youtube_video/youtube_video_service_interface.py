from abc import ABC, abstractmethod
from app.domain.entities.video_source import VideoSource
from app.domain.utils.response import Response


class YoutubeVideoServiceInterface(ABC):
    @abstractmethod
    async def download(self, video_url: str) -> Response[VideoSource]:
        pass
