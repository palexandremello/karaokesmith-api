from domain.entities.mp3_file import Mp3File
from domain.entities.youtube_audio import YoutubeAudio
from domain.usecases.get_youtube_video.get_youtube_video_interface import GetYoutubeVideoUseCaseInterface
from domain.usecases.video_to_audio_converter.video_to_audio_converter_interface import (
    VideoToAudioConverterUseCaseInterface,
)
from domain.usecases.youtube_audio.youtube_audio_interface import YoutubeAudioUseCaseInterface
from domain.utils.response import Response


class YoutubeAudioUseCase(YoutubeAudioUseCaseInterface):
    def __init__(
        self,
        get_youtube_video_usecase: GetYoutubeVideoUseCaseInterface,
        video_to_audio_converter_usecase: VideoToAudioConverterUseCaseInterface,
    ) -> None:
        self.get_video_use_case = get_youtube_video_usecase
        self.convert_video_to_audio_use_case = video_to_audio_converter_usecase

    async def execute(self, video_url: str) -> Response[YoutubeAudio]:
        video_response = await self.get_video_use_case.get(video_url)

        if not video_response.success:
            return Response(success=False, body=video_response.body)

        converted_video_response = await self.convert_video_to_audio_use_case.convert(video_response.body)

        if not converted_video_response.success:
            return Response(success=False, body=converted_video_response.body)

        mp3_file = Mp3File(name=video_response.body.title, path=converted_video_response.body.path)
        youtube_audio = YoutubeAudio(video_url=video_url, mp3_file=mp3_file)

        return Response(success=True, body=youtube_audio)
