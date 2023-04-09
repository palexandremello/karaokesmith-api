from typing import Dict


class HttpRequest:
    def __init__(self, header: Dict = None, body: Dict = None, form: Dict = None, query: Dict = None) -> None:
        self.header = header
        self.body = body
        self.form = form
        self.query = query

        def __repr__(self) -> str:
            return f"HttpRequest (header={self.header}, body={self.body}, form={self.form} query={self.query})"
