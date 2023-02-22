from typing import Dict
from unittest.mock import patch
import pytest
import pytest_asyncio
from infrastructure.gateways.ytdlp_video_downloader import YtDlpVideoDownloader


class TestYtDlpVideoDownloader:
    @pytest_asyncio.fixture
    def mock_youtube_dl(self):
        return {"title": "mocked_video_title", "thumbnail": "mocked_thumbnail_url"}

    @pytest.fixture
    def mock_download(self):
        return [{"filepath": "any_path"}]

    @pytest_asyncio.fixture
    def ytdlp_video_downloader_stub(self) -> YtDlpVideoDownloader:
        return YtDlpVideoDownloader()

    @pytest.mark.asyncio
    async def test_should_be_able_to_returns_VideoMetadata_from_get_video_info(
        self,
        ytdlp_video_downloader_stub: YtDlpVideoDownloader,
        mock_youtube_dl: Dict[str, str],
    ):
        with patch("yt_dlp.YoutubeDL.extract_info", return_value=mock_youtube_dl):
            video_metadata = await ytdlp_video_downloader_stub.get_video_info(
                "any_video_url"
            )

        assert video_metadata.title == "mocked_video_title"
        assert video_metadata.thumbnail_url == "mocked_thumbnail_url"

    @pytest.mark.asyncio
    async def test_should_raises_KeyError_when_extract_info_returns_empty_dict(
        self,
        ytdlp_video_downloader_stub: YtDlpVideoDownloader,
    ):
        with patch("yt_dlp.YoutubeDL.extract_info", return_value={}):
            with pytest.raises(KeyError, match="any video metadata"):
                await ytdlp_video_downloader_stub.get_video_info("any_video_url")

    @pytest.mark.asyncio
    async def test_should_be_able_to_returns_a_filepath_when_get_video_is_successful(
        self,
        ytdlp_video_downloader_stub: YtDlpVideoDownloader,
    ):
        with patch(
            "yt_dlp.YoutubeDL.download", return_value=[{"filepath": "any_path"}]
        ):
            path = await ytdlp_video_downloader_stub.get_video("any_video_url")

            assert path == "any_path"
