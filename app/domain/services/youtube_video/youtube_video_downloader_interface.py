from abc import ABC, abstractmethod
from domain.entities.video_metadata import VideoMetadata


class YoutubeDownloaderInterface(ABC):

    @abstractmethod
    def get_video(self, video_url: str) -> str:
        pass

    @abstractmethod
    def get_video_info(self, video_url: str) -> VideoMetadata:
        pass