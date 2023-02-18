

from typing import Union
from unittest import mock 
from unittest.mock import AsyncMock, MagicMock, Mock
import pytest

import pytest_asyncio
from domain.services.mp3_file.mp3_file_service import Mp3FileService
from domain.services.mp3_file.mp3_file_validator_interface import Mp3FileValidatorInterface



class TestMp3FileService:

    @pytest_asyncio.fixture
    def mp3_file_validator_stub(self) -> Mp3FileValidatorInterface:
        return AsyncMock(spec=Mp3FileValidatorInterface)
    

    @pytest_asyncio.fixture
    def mp3_file_service(self, mp3_file_validator_stub):
        return Mp3FileService(mp3_file_validator_stub)
    
    @pytest.mark.asyncio
    async def test_should_return_None_when_validate_is_correct(self, mp3_file_service,
                                                         mp3_file_validator_stub):
         
         mp3_file_validator_stub.validate = AsyncMock(return_value=None)

         response = await mp3_file_service.validate_mp3_file("ANY_PATH")

         assert response is None

    @pytest.mark.asyncio
    async def test_should_raise_exception_when_validate_is_incorrect(self, mp3_file_service,
                                                               mp3_file_validator_stub):
        
        expected_error = Exception("validation error")

        mp3_file_validator_stub.validate = AsyncMock(side_effect=expected_error)

    
        error = await mp3_file_service.validate_mp3_file("ANY_PATH")
        
        assert isinstance(error, Exception)
        
        assert error == expected_error
