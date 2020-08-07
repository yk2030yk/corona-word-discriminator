from typing import Optional
from .request_base import RequestBase
from cotoha_api.validator import Validator


class SummaryRequest(RequestBase):
    def __init__(self, document: str, sent_len: int):
        self.document = document
        self.sent_len = sent_len

    def validate(self):
        pass

    def to_dict(self):
        return {"document": self.document, "sent_len": self.sent_len}
