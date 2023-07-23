import os
import ffmpeg
from app.domain.entities.video_source import VideoSource
from app.domain.services.video_converter.converter_interface import ConverterInterface
from app.domain.utils.logger.logger_interface import LoggerInterface


class FFmpegConverter(ConverterInterface):
    """
    Implementação do conversor de vídeos FFmpeg.

    Args:
        logger (LoggerInterface): Objeto responsável por logar mensagens de erro, informação e debug.

    Attributes:
        logger (LoggerInterface): Objeto responsável por logar mensagens de erro, informação e debug.
    """

    def __init__(self, logger: LoggerInterface) -> None:
        """
        Inicializa o objeto FFmpegConverter.

        Args:
            logger (LoggerInterface): Objeto responsável por logar mensagens de erro, informação e debug.
        """
        self.logger = logger

    def execute(self, video: VideoSource) -> str:
        """
        Executa a conversão de um arquivo de vídeo em um arquivo de áudio.

        Args:
            video (VideoSource): Objeto representando o arquivo de vídeo que será convertido.

        Returns:
            str: Caminho do arquivo de áudio convertido.
        """
        audio_path = os.path.splitext(video.path)[0] + ".mp3"
        self.logger.debug(f"Starting ffmpeg converter to path = {audio_path}")

        stream = ffmpeg.input(video.path)
        stream = ffmpeg.output(stream, audio_path, acodec="libmp3lame", loglevel="error")
        ffmpeg.run(stream)

        return audio_path
