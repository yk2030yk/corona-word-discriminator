from .response_base import ResponseBase


class NeResponse(ResponseBase):
    def __init__(self, response_json):
        super().__init__(response_json)
        self.result = Result(response_json)


class Result(object):
    def __init__(self, response_json):
        self.objects = [NeObject(r) for r in response_json.get("result", [])]


class NeObject(object):
    def __init__(self, response_json):
        self.begin_pos = response_json.get("begin_pos")
        self.end_pos = response_json.get("end_pos")
        self.form = response_json.get("form")
        self.std_form = response_json.get("std_form")
        self.entity_class = response_json.get("class")
        self.extended_entity_class = response_json.get("extended_class")
        self.info = response_json.get("info")
        self.source = response_json.get("source")
