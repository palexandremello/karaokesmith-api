from application.controllers.interface.controller_interface import ControllerInterface
from application.helpers.http.request import HttpRequest
from application.helpers.http.response import HttpResponse
from domain.usecases.sample.sample_interface import SampleUseCaseInterface


class CreateSampleController(ControllerInterface):
    def __init__(
        self,
        sample_usecase: SampleUseCaseInterface,
    ) -> None:
        self.sample_usecase = sample_usecase

    async def handle(self, http_request: HttpRequest) -> HttpResponse:
        try:
            minutes_per_sample = http_request.form.get("minutes_per_sample")
            name = http_request.form.get("name")
            video_url = http_request.form.get("video_url")
            upload_mp3_file = http_request.form.get("upload_mp3_file")

            response = await self.sample_usecase.execute(minutes_per_sample, name, video_url, upload_mp3_file)

            if not response.success:
                return HttpResponse(status_code=400, body={"error": response.body})

            return HttpResponse(status_code=201, body=response.body)

        except Exception as e:
            return HttpResponse(status_code=500, body={"error": str(e)})
