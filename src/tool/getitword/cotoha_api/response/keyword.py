from .response_base import ResponseBase


class KeywordResponse(ResponseBase):
    def __init__(self, response_json: dict):
        super().__init__(response_json)
        self.result = Result(response_json)


class Result(object):
    def __init__(self, response_json: dict):
        self.objects = [KeyworbObject(r) for r in response_json.get("result", [])]


class KeyworbObject(object):
    def __init__(self, response_json: dict):
        self.form = response_json.get("form")
        self.score = response_json.get("score")
