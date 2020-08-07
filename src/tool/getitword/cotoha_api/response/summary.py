from .response_base import ResponseBase


class SummaryResponse(ResponseBase):
    def __init__(self, response_json: dict):
        super().__init__(response_json)
        self.result = response_json.get("result")
