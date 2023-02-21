

from abc import ABC, abstractmethod

from domain.entities.video_source import VideoSource


class ConverterInterface(ABC):

    @abstractmethod
    async def execute(self, video: VideoSource) -> str:
        pass