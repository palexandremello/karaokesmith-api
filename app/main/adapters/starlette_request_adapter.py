from app.application.adapters.request_adapter_interface import RequestAdapterInterface
from app.application.helpers.http.request import HttpRequest


class StarletteRequestAdapter(RequestAdapterInterface):
    async def adapt(self, request: any) -> HttpRequest:
        header = request.headers
        body = await request.body()
        form_dict = dict(await request.form())
        query = request.query_params

        upload_mp3_file = form_dict.get("upload_mp3_file")

        if upload_mp3_file:
            content = await upload_mp3_file.read()
            form_dict["upload_mp3_file"] = content

        return HttpRequest(header=header, body=body, form=form_dict, query=query)
