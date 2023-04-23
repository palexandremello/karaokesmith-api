from typing import List
from app.domain.entities.sample import Sample
from app.domain.services.sample_saver.sample_saver_interface import SampleSaverInterface
from app.domain.services.sample_saver.save_method_interface import SaveMethodInterface
from app.domain.utils.response import Response


class SampleSaver(SampleSaverInterface):
    def __init__(self, save_method: SaveMethodInterface) -> None:
        self.save_method = save_method

    def save_sample(self, samples: List[Sample]) -> Response[List[Sample]]:
        response = self.save_method.save(samples=samples)

        if not response.success:
            return Response(success=False, body=response.body)

        return response
