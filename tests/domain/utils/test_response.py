import dataclasses

from app.domain.utils.response import Response


@dataclasses.dataclass
class AnyEntityClass:
    status_code: int
    body: str


BODY = AnyEntityClass(200, "any_body")
EXPECTED_RESPONSE = {"success": True, "body": {"status_code": 200, "body": "any_body"}}


def test_should_be_same_instance_of_Response():
    use_case_response = Response(success=True, body=BODY)

    assert isinstance(use_case_response, Response)


def test_should_be_able_to_return_a_dictionary_response():
    use_case_response = Response(success=True, body=BODY)

    use_case_response.body
    response = use_case_response.to_dict()
    assert response == EXPECTED_RESPONSE
