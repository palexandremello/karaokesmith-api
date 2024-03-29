from unittest.mock import AsyncMock
import pytest
import pytest_asyncio
from app.domain.entities.sample import Sample
from app.domain.services.create_sample_service.create_sample_service_interface import CreateSampleServiceInterface
from app.domain.usecases.create_sample_from_mp3.create_sample_from_mp3_interface import (
    CreateSampleFromMp3UseCaseInterface,
)
from app.domain.usecases.create_sample_from_youtube.create_sample_from_youtube_interface import (
    CreateSampleFromYoutubeUseCaseInterface,
)
from app.domain.usecases.sample.sample_impl import SampleUseCase
from app.domain.usecases.save_sample.save_sample_interface import SaveSampleUseCaseInterface
from app.domain.utils.response import Response


class TestSampleUseCase:
    sample = Sample(name="any_artist", path="any_path")

    @pytest_asyncio.fixture
    def create_sample_service_stub(self):
        return AsyncMock(spec=CreateSampleServiceInterface)

    @pytest_asyncio.fixture
    def create_sample_from_mp3_usecase_stub(self):
        return AsyncMock(spec=CreateSampleFromMp3UseCaseInterface)

    @pytest_asyncio.fixture
    def save_sample_usecase_stub(self):
        return AsyncMock(spec=SaveSampleUseCaseInterface)

    @pytest_asyncio.fixture
    def create_sample_from_youtube_usecase_stub(self):
        return AsyncMock(spec=CreateSampleFromYoutubeUseCaseInterface)

    @pytest_asyncio.fixture
    def sample_usecase(
        self,
        create_sample_from_mp3_usecase_stub,
        create_sample_from_youtube_usecase_stub,
        save_sample_usecase_stub,
    ):
        return SampleUseCase(
            create_sample_from_mp3_usecase=create_sample_from_mp3_usecase_stub,
            create_sample_from_youtube_usecase=create_sample_from_youtube_usecase_stub,
            save_sample_usecase=save_sample_usecase_stub,
        )

    @pytest.mark.asyncio
    async def test_should_be_able_to_create_a_sample_from_youtube_usecase(
        self, sample_usecase: SampleUseCase, create_sample_from_youtube_usecase_stub, save_sample_usecase_stub
    ):
        create_sample_from_youtube_usecase_stub.execute = AsyncMock(
            return_value=Response(success=True, body=self.sample)
        )

        save_sample_usecase_stub.save = AsyncMock(return_value=Response(success=True, body=self.sample))
        response = await sample_usecase.execute(
            name=None,
            minutes_per_sample=5,
            video_url="ANY_URL",
        )

        assert response.success
        assert response.body == self.sample

    @pytest.mark.asyncio
    async def test_should_be_able_to_create_a_sample_from_mp3_usecase(
        self, sample_usecase: SampleUseCase, create_sample_from_mp3_usecase_stub, save_sample_usecase_stub
    ):
        create_sample_from_mp3_usecase_stub.execute = AsyncMock(
            return_value=Response(success=True, body=self.sample_with_mp3)
        )

        save_sample_usecase_stub.save = AsyncMock(return_value=Response(success=True, body=self.sample_with_mp3))

        response = await sample_usecase.execute(
            name=None,
            minutes_per_sample=5,
            upload_mp3_file="any_mp3_uploaded",
        )

        assert response.success
        assert response.body == self.sample_with_mp3

    @pytest.mark.asyncio
    async def test_should_return_a_response_with_error_when_create_samples_usecase_throws(
        self, sample_usecase: SampleUseCase, create_sample_from_mp3_usecase_stub, save_sample_usecase_stub
    ):
        create_sample_from_mp3_usecase_stub.execute = AsyncMock(return_value=Response(success=False, body="any_error"))
        save_sample_usecase_stub.save = AsyncMock(return_value=Response(success=False, body="any_error"))

        response = await sample_usecase.execute(
            name=None,
            minutes_per_sample=5,
            upload_mp3_file="any_mp3_uploaded",
        )

        assert not response.success
        assert response.body == "any_error"
