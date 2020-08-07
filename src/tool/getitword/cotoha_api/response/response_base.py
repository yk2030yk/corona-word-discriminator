STATUS_OK = 0


class ResponseBase(object):
    def __init__(self, response_json):
        self.status = response_json.get("status")
        self.message = response_json.get("message")

    @property
    def has_error(self):
        return self.status != STATUS_OK

    def validate(self):
        if self.has_error:
            raise Exception("aaaa")
