from typing import Optional
from .request_base import RequestBase


TYPES = ["default", "kuzure"]
DIC_TYPES = [
    "IT",
    "automobile",
    "chemistry",
    "company",
    "construction",
    "economy",
    "energy",
    "institution",
    "machinery",
    "medical",
    "metal",
]


class NeRequest(RequestBase):
    def __init__(
        self, sentence: str, type: Optional[str] = None, dic_type: Optional[str] = None
    ):
        self.sentence = sentence
        self.type = type
        self.dic_type = dic_type

    def validate(self):
        pass

    def to_dict(self):
        return {"sentence": self.sentence, "type": self.type, "dic_type": self.dic_type}
