
import dataclasses

from domain.utils.use_case_response import UseCaseResponse

@dataclasses.dataclass
class AnyEntityClass:
    status_code: int
    body: str

BODY = AnyEntityClass(200, "any_body")
EXPECTED_RESPONSE = {"success": True, "body": {'status_code': 200, 'body': 'any_body'}}

def test_should_be_same_instance_of_UseCaseResponse():
    use_case_response = UseCaseResponse(success=True, body=BODY)

    assert isinstance(use_case_response, UseCaseResponse)


def test_should_be_able_to_return_a_dictionary_response():
    use_case_response = UseCaseResponse(success=True, body=BODY)

    response = use_case_response.to_dict()
    assert response == EXPECTED_RESPONSE