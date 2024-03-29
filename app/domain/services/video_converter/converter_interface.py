from abc import ABC, abstractmethod

from app.domain.entities.video_source import VideoSource


class ConverterInterface(ABC):
    @abstractmethod
    def execute(self, video: VideoSource) -> str:
        pass
