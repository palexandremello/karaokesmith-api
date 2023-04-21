from app.application.controllers.interface.controller_interface import ControllerInterface
from app.application.helpers.http.request import HttpRequest
from app.application.helpers.http.response import HttpResponse
from app.domain.usecases.sample.sample_interface import SampleUseCaseInterface
from app.domain.entities.mp3_file import Mp3File
import traceback


class CreateSampleController(ControllerInterface):
    def __init__(
        self,
        sample_usecase: SampleUseCaseInterface,
    ) -> None:
        self.sample_usecase = sample_usecase

    async def handle(self, http_request: HttpRequest) -> HttpResponse:
        try:
            video_url = http_request.form.get("video_url")
            minutes_per_sample = int(http_request.form.get("minutes_per_sample"))
            name = http_request.form.get("name")
            mp3_file = http_request.form.get("upload_mp3_file")
            upload_mp3_file = Mp3File(name=name, path=mp3_file)

            response = await self.sample_usecase.execute(minutes_per_sample, name, video_url, upload_mp3_file)
            if not response.success:
                return HttpResponse(status_code=400, body={"error": response.body})

            return HttpResponse(status_code=201, body=response.body)

        except Exception as e:
            traceback.print_exc()
            return HttpResponse(status_code=500, body={"error": str(e)})
