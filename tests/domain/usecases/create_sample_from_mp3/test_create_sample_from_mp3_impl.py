from unittest.mock import AsyncMock
import pytest
import pytest_asyncio
from app.domain.entities.mp3_file import Mp3File
from app.domain.services.create_sample_service.create_sample_service_interface import CreateSampleServiceInterface
from app.domain.usecases.create_sample_from_mp3.create_sample_from_mp3_impl import CreateSampleFromMp3UseCase
from app.domain.usecases.mp3_file.mp3_file_interface import Mp3FileUseCaseInterface
from app.domain.utils.response import Response


class TestCreateSampleFromMp3:
    mp3_file = Mp3File("Tevin Campbell, Rosie Gaines - I2I", path="any_path")
    minutes_per_sample = 1

    @pytest_asyncio.fixture
    def mp3_file_usecase_stub(self):
        return AsyncMock(spec=Mp3FileUseCaseInterface)

    @pytest_asyncio.fixture
    def create_sample_service_stub(self):
        return AsyncMock(spec=CreateSampleServiceInterface)

    @pytest_asyncio.fixture
    def create_sample_from_mp3_usecase(
        self, mp3_file_usecase_stub, create_sample_service_stub
    ) -> CreateSampleFromMp3UseCase:
        return CreateSampleFromMp3UseCase(
            mp3_file_usecase=mp3_file_usecase_stub,
            create_sample_service=create_sample_service_stub,
        )

    @pytest.mark.asyncio
    async def test_should_be_able_create_a_sample_from_upload_mp3_file(
        self,
        mp3_file_usecase_stub,
        create_sample_service_stub,
        create_sample_from_mp3_usecase,
    ):
        mp3_file_usecase_stub.execute = AsyncMock(return_value=Response(success=True, body=self.mp3_file))

        create_sample_service_stub.execute = AsyncMock(return_value=Response(success=True, body="any_body"))

        response = await create_sample_from_mp3_usecase.execute(self.mp3_file, self.minutes_per_sample)

        assert response.success
        assert response.body == "any_body"

    @pytest.mark.asyncio
    async def test_should_return_response_with_error_when_mp3_file_usecase_fails(
        self,
        mp3_file_usecase_stub,
        create_sample_from_mp3_usecase,
    ):
        mp3_file_usecase_stub.execute = AsyncMock(return_value=Response(success=False, body="any_error"))

        response = await create_sample_from_mp3_usecase.execute(self.mp3_file, self.minutes_per_sample)

        assert not response.success
        assert response.body == "any_error"

    @pytest.mark.asyncio
    async def test_should_return_response_with_error_when_create_sample_service_fails(
        self,
        mp3_file_usecase_stub,
        create_sample_service_stub,
        create_sample_from_mp3_usecase,
    ):
        mp3_file_usecase_stub.execute = AsyncMock(return_value=Response(success=True, body=self.mp3_file))
        create_sample_service_stub.execute = AsyncMock(return_value=Response(success=False, body="any_sample_error"))

        response = await create_sample_from_mp3_usecase.execute(self.mp3_file, self.minutes_per_sample)

        assert not response.success
        assert response.body == "any_sample_error"
