import pytest
from domain.utils.service_response import ServiceResponse


class TestServiceResponse:

    @pytest.fixture
    def error(self) -> dict:
        return {"success": False, "error_message": "Any Error"}
    
    @pytest.fixture
    def successful(self) -> dict:
        return {"success": True, "error_message": None}
    
    def test_should_be_able_to_return_a_dict_response_when_service_throws_error(self, error):
        sut = ServiceResponse(success=error["success"], error_message=error["error_message"])

        dict_to_be_assert = sut.to_dict()

        assert dict_to_be_assert == error