import asyncio
from tempfile import TemporaryDirectory
from yt_dlp import YoutubeDL
from app.domain.entities.video_metadata import VideoMetadata

from app.domain.services.youtube_video.youtube_video_downloader_interface import (
    YoutubeDownloaderInterface,
)


class YtDlpVideoDownloader(YoutubeDownloaderInterface):
    def __init__(self) -> None:
        self._tmp_dir = TemporaryDirectory().name
        self.__options = {"outtmpl": f"{self._tmp_dir}/%(title)s%(ext)s"}
        self.youtube_dl: YoutubeDL = YoutubeDL(self.__options)

    async def get_video(self, video_url: str) -> str:
        with self.youtube_dl:
            result = await asyncio.get_event_loop().run_in_executor(
                None, lambda: self.youtube_dl.download([video_url])
            )

            if len(result) == 0:
                raise FileExistsError("it was not able to retrieve video content")

            return result[0]["filepath"]

    async def get_video_info(self, video_url: str) -> VideoMetadata:
        with self.youtube_dl:
            result = await asyncio.get_event_loop().run_in_executor(
                None, lambda: self.youtube_dl.extract_info(video_url, download=False)
            )
            video_title = result.get("title", None)
            video_thumbnail = result.get("thumbnail", None)

        if video_thumbnail is None or video_title is None:
            raise KeyError("any video metadata")

        return VideoMetadata(title=video_title, thumbnail_url=video_thumbnail)
