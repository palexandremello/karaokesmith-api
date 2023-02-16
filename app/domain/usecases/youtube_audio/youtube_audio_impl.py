
from domain.entities.youtube_audio import YoutubeAudio
from domain.usecases.youtube_audio.youtube_audio_interface import YoutubeAudioUseCaseInterface

#GetVideoUseCaseInterface
#ConvertVideoToAudioUseCaseInterface
class YoutubeAudioUseCaseImpl(YoutubeAudioUseCaseInterface):
    def __init__(self, get_video_use_case: any,
                 convert_video_to_audio_use_case: any) -> None:
        self.get_video_use_case = get_video_use_case
        self.convert_video_to_audio_use_case = convert_video_to_audio_use_case

    def execute(self, link: str) -> YoutubeAudio:

        video = self.get_video_use_case.execute(link)

        mp3_file = self.convert_video_to_audio_use_case(video)

        return YoutubeAudio(link=link, name=video.name, mp3_file=mp3_file)