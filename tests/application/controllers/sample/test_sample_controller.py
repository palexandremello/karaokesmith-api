from unittest.mock import AsyncMock
import pytest
import pytest_asyncio
from application.controllers.create_sample.create_sample_controller import CreateSampleController
from application.helpers.http.request import HttpRequest
from domain.entities.youtube_audio import YoutubeAudio
from domain.usecases.sample.sample_interface import SampleUseCaseInterface
from domain.entities.sample import Sample
from domain.utils.response import Response


class TestCreateSampleController:
    @pytest_asyncio.fixture
    def sample_youtube(self):
        name = "Silent Screamer - Tatsurō Yamashita"
        video_url = "https://www.youtube.com/watch?v=_pNqMc6NVAE"
        return Sample(
            audio_option=YoutubeAudio(video_url=video_url),
            name=name,
            content=b"any_bytes",
            path="any_path",
            id="any_id",
        )

    @pytest_asyncio.fixture
    def sample_usecase_stub(self):
        return AsyncMock(spec=SampleUseCaseInterface)

    @pytest_asyncio.fixture
    def create_sample_controller(self, sample_usecase_stub):
        return CreateSampleController(sample_usecase=sample_usecase_stub)

    @pytest.mark.asyncio
    async def test_should_return_201_and_sample_when_sample_creation_succeeds(
        self,
        create_sample_controller,
        sample_usecase_stub,
        sample_youtube,
    ):
        # Arrange
        minutes_per_sample = "1"
        name = "Silent Screamer - Tatsurō Yamashita"
        video_url = "https://www.youtube.com/watch?v=_pNqMc6NVAE"

        http_request = HttpRequest(
            form={
                "minutes_per_sample": minutes_per_sample,
                "name": name,
                "video_url": video_url,
            }
        )

        sample_usecase_stub.execute = AsyncMock(return_value=Response(success=True, body=sample_youtube))

        # Act
        response = await create_sample_controller.handle(http_request)
        assert response.status_code == 201
        assert response.body == sample_youtube
