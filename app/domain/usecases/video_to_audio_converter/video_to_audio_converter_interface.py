from abc import ABC, abstractmethod
from domain.entities.audio_media import AudioMedia
from domain.entities.video_source import VideoSource

from domain.utils.use_case_response import UseCaseResponse

class VideoToAudioConverterUseCaseInterface(ABC):

    @abstractmethod
    def convert(self, video: VideoSource) -> UseCaseResponse[AudioMedia]:
        pass