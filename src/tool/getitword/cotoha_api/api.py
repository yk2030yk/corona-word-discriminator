import json
from enum import Enum, auto
from typing import Optional
import requests
from .util import filter_dict
from .errors import CotohaApiError
from .oauth import CotohaApiOAuth
from .client_credentials import ClientCredentials


API_BASE_URL = "https://api.ce-cotoha.com/api/dev"
DEFAULT_HEADERS = {"Accept-Language": "ja-JP"}


class API_TYPE(Enum):
    NE = auto()
    KEYWORD = auto()
    SUMMARY = auto()


API_URI = {
    API_TYPE.NE: "/nlp/v1/ne",
    API_TYPE.KEYWORD: "/nlp/v1/keyword",
    API_TYPE.SUMMARY: "/nlp/beta/summary",
}


class CotohaApi(object):
    def __init__(self, client_credentials: ClientCredentials):
        self.oauth: CotohaApiOAuth = CotohaApiOAuth(client_credentials)

    def _create_api_url(self, api_type: API_TYPE) -> str:
        if api_type not in API_URI:
            raise CotohaApiError("")

        return f"{API_BASE_URL}{API_URI.get(api_type)}"

    def _post(self, api_type: API_TYPE, data: dict, headers: dict = {}) -> dict:
        access_token = self.oauth.get_access_token()

        headers.update(DEFAULT_HEADERS)
        headers.update(access_token.authorization_header)

        try:
            response = requests.post(
                self._create_api_url(api_type), json=filter_dict(data), headers=headers,
            )
        except Exception as e:
            raise CotohaApiError(e)

        return response.json()

    def get_ne(
        self, sentence: str, type: Optional[str] = None, dic_type: Optional[str] = None
    ) -> dict:
        return self._post(
            API_TYPE.NE, {"sentence": sentence, "type": type, "dic_type": dic_type}
        )

    def get_keyword(
        self,
        document: str,
        type: Optional[str] = None,
        do_segment: Optional[str] = None,
        max_keyword_num: Optional[int] = None,
        dic_type: Optional[str] = None,
    ) -> dict:
        return self._post(
            API_TYPE.KEYWORD,
            {
                "document": document,
                "type": type,
                "do_segment": do_segment,
                "max_keyword_num": max_keyword_num,
                "dic_type": dic_type,
            },
        )

    def get_summary(self, document: str, sent_len: int) -> dict:
        return self._post(
            API_TYPE.SUMMARY, {"document": document, "sent_len": sent_len}
        )
