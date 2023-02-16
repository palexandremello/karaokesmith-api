
import dataclasses

from domain.utils.use_case_response import UseCaseReponse

@dataclasses.dataclass
class AnyEntityClass:
    pass

def should_be_same_instance_of_AnyEntityClass():
    use_case_response = UseCaseReponse(AnyEntityClass)

    assert isinstance(use_case_response, AnyEntityClass)
