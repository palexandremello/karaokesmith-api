

from abc import ABC, abstractmethod
from domain.entities.audio_media import AudioFormat

from domain.entities.video_source import VideoSource


class VideoConverterServiceInterface(ABC):

    @abstractmethod
    def execute(self, video: VideoSource) -> AudioFormat:
        pass