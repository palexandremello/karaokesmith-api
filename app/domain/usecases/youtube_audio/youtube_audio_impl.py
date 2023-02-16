
from typing import Optional
from domain.entities.youtube_audio import YoutubeAudio
from domain.usecases.get_youtube_video.get_youtube_video_interface import GetYoutubeVideoUseCaseInterface
from domain.usecases.video_to_audio_converter.video_to_audio_converter_interface import VideoToAudioConverterUseCaseInterface
from domain.usecases.youtube_audio.youtube_audio_interface import YoutubeAudioUseCaseInterface
from domain.utils.use_case_response import UseCaseResponse

class YoutubeAudioUseCaseImpl(YoutubeAudioUseCaseInterface):
    def __init__(self, get_youtube_video_usecase: GetYoutubeVideoUseCaseInterface,
                 video_to_audio_converter_usecase: VideoToAudioConverterUseCaseInterface) -> None:
        self.get_video_use_case = get_youtube_video_usecase
        self.convert_video_to_audio_use_case = video_to_audio_converter_usecase

    
    def execute(cls, link: str, name: Optional[str] = None) -> UseCaseResponse[YoutubeAudio]:
        pass