from app.application.controllers.interface.controller_interface import ControllerInterface
from app.application.helpers.http.request import HttpRequest
from app.application.helpers.http.response import HttpResponse
from app.domain.usecases.sample.sample_interface import SampleUseCaseInterface
from app.domain.utils.logger.logger_interface import LoggerInterface


class CreateSampleController(ControllerInterface):
    def __init__(self, sample_usecase: SampleUseCaseInterface, logger: LoggerInterface) -> None:
        self.sample_usecase = sample_usecase
        self.logger = logger

    def handle(self, http_request: HttpRequest) -> HttpResponse:
        try:
            video_url = http_request.form.get("video_url")
            minutes_per_sample = int(http_request.form.get("minutes_per_sample"))
            name = http_request.form.get("name")
            upload_mp3_file = http_request.form.get("upload_mp3_file")

            response = self.sample_usecase.execute(minutes_per_sample, name, video_url, upload_mp3_file)
            if not response.success:
                return HttpResponse(status_code=400, body={"error": response.body})

            return HttpResponse(status_code=201, body=response.body)

        except Exception as e:
            self.logger.error(f"error something happening = {e}")
            return HttpResponse(status_code=500, body={"error": str(e)})
