

from abc import ABC, abstractmethod

from domain.entities.video_source import VideoSource


class YoutubeVideoServiceInterface(ABC):

    @abstractmethod
    async def download(self, url: str) -> VideoSource:
        pass

