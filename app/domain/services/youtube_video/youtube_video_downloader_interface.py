from abc import ABC, abstractmethod
from domain.entities.video_source import VideoSource


class YoutubeDownloaderInterface(ABC):

    @abstractmethod
    def get_video(self, url: str) -> VideoSource:
        pass

    @abstractmethod
    def get_video_info(self, url: str) -> dict:
        pass