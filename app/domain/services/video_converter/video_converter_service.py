
from typing import Union
from domain.entities.audio_media import AudioMedia
from domain.entities.video_source import VideoSource
from domain.services.video_converter.converter_interface import ConverterInterface
from domain.utils.response import Response
from .video_converter_service_interface import VideoConverterServiceInterface

class VideoConverterService(VideoConverterServiceInterface):

    def __init__(self, converter: ConverterInterface) -> None:
        self.converter = converter

    
    async def execute(self, video: VideoSource) -> Union[Response[AudioMedia],
                                                         Response[Exception]]:
        try:
           
           path = await self.converter.execute(video)
           audio_media = AudioMedia.from_dict({"path": path, "audio_format": "mp3"})
           return Response(success=True, body=audio_media)
        
        except Exception as error:
            return Response(success=False, body=str(error))