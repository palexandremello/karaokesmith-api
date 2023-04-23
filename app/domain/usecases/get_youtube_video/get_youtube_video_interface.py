from abc import ABC, abstractmethod
from app.domain.entities.video_source import VideoSource
from app.domain.utils.response import Response


class GetYoutubeVideoUseCaseInterface(ABC):
    @abstractmethod
    def get(self, video_url: str) -> Response[VideoSource]:
        pass
