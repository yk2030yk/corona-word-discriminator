from typing import Optional
from .api import CotohaApi
from .request import NeRequest, KeywordRequest, SummaryRequest
from .response import KeywordResponse, NeResponse, SummaryResponse
from cotoha_api.errors import CotohaApiError


class CotohaApiService(object):
    def __init__(self, client_credentials):
        self.api = CotohaApi(client_credentials)

    def get_ne(
        self, sentence: str, type: Optional[str] = None, dic_type: Optional[str] = None
    ) -> dict:
        request = NeRequest(sentence, type, dic_type)

        response_json = self.api.get_ne(**request.to_dict())
        response = NeResponse(response_json)
        response.validate()

        return response

    def get_keyword(
        self,
        document: str,
        type: Optional[str] = None,
        do_segment: Optional[str] = None,
        max_keyword_num: Optional[int] = None,
        dic_type: Optional[str] = None,
    ) -> dict:
        request = KeywordRequest(document, type, do_segment, max_keyword_num, dic_type)

        response_json = self.api.get_keyword(**request.to_dict())
        response = KeywordResponse(response_json)
        response.validate()

        return response

    def get_summary(self, document: str, sent_len: int) -> dict:
        request = SummaryRequest(document, sent_len)

        response_json = self.api.get_summary(**request.to_dict())
        response = SummaryResponse(response_json)
        response.validate()

        return response
