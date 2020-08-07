from typing import Optional
from .request_base import RequestBase


class KeywordRequest(RequestBase):
    def __init__(
        self,
        document: str,
        type: Optional[str] = None,
        do_segment: Optional[str] = None,
        max_keyword_num: Optional[int] = None,
        dic_type: Optional[str] = None,
    ):
        self.document = document
        self.type = type
        self.do_segment = do_segment
        self.max_keyword_num = max_keyword_num
        self.dic_type = dic_type

    def validate(self):
        pass

    def to_dict(self):
        return {
            "document": self.document,
            "type": self.type,
            "do_segment": self.do_segment,
            "max_keyword_num": self.max_keyword_num,
            "dic_type": self.dic_type,
        }
