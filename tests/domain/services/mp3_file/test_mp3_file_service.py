import pytest
import pytest_asyncio
from unittest.mock import AsyncMock
from domain.services.mp3_file.mp3_file_service import Mp3FileService
from domain.services.mp3_file.mp3_file_validator_interface import Mp3FileValidatorInterface
from domain.utils.service_response import ServiceResponse


class TestMp3FileService:

    @pytest_asyncio.fixture
    def mp3_file_validator_stub(self) -> Mp3FileValidatorInterface:
        return AsyncMock(spec=Mp3FileValidatorInterface)
    
    @pytest.fixture
    def correct_validate_response(self):
        return ServiceResponse(success=True, error_message=None)
    
    @pytest.fixture
    def incorrect_validate_response(self):
        return ServiceResponse(success=False, error_message="MP3 file is invalid")

    @pytest_asyncio.fixture
    def mp3_file_service(self, mp3_file_validator_stub):
        return Mp3FileService(mp3_file_validator_stub)
    
    @pytest.mark.asyncio
    async def test_should_return_None_when_validate_is_correct(self, mp3_file_service,
                                                         mp3_file_validator_stub,
                                                         correct_validate_response):
         
         mp3_file_validator_stub.validate = AsyncMock(return_value=None)

         response = await mp3_file_service.validate_mp3_file("ANY_PATH")

         assert response == correct_validate_response

    @pytest.mark.asyncio
    async def test_should_raise_exception_when_validate_is_incorrect(self, mp3_file_service,
                                                               mp3_file_validator_stub,
                                                               incorrect_validate_response):
        
        expected_error = ValueError("MP3 file is invalid")

        mp3_file_validator_stub.validate = AsyncMock(side_effect=expected_error)
    
        response = await mp3_file_service.validate_mp3_file("ANY_PATH")
                
        assert response == incorrect_validate_response
