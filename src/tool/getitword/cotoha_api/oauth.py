from datetime import datetime
import requests
from .errors import CotohaApiError
from .client_credentials import ClientCredentials


ACCESS_TOKEN_PUBLISH_URL = "https://api.ce-cotoha.com/v1/oauth/accesstokens"


def calc_expired_at(issued_at: str, expires_in: str):
    if issued_at is None or expires_in is None:
        return None
    return datetime.fromtimestamp(int(issued_at) / 1000 + int(expires_in))


class AccessToken(object):
    def __init__(self, response_json: dict = {}):
        self.access_token = response_json.get("access_token")
        self.expires_in = response_json.get("expires_in")
        self.issued_at = response_json.get("issued_at")
        self.expired_at = calc_expired_at(self.issued_at, self.expires_in)

    @property
    def is_available(self) -> bool:
        return (
            self.access_token is not None
            and self.expired_at
            and datetime.now() < self.expired_at
        )

    @property
    def authorization_header(self) -> dict:
        if self.access_token is None:
            return {}
        return {"Authorization": f"Bearer {self.access_token}"}


class CotohaApiOAuth(object):
    def __init__(self, client_credentials: ClientCredentials):
        self.client_credentials: ClientCredentials = client_credentials
        self._access_token = AccessToken()

    def _fetch_access_token(self) -> None:
        if self._access_token.is_available:
            return

        response = requests.post(
            ACCESS_TOKEN_PUBLISH_URL, json=self.client_credentials.to_dict()
        )
        response_json = response.json()

        if "access_token" not in response_json:
            raise CotohaApiError("could not get access token.")

        self._access_token = AccessToken(response_json)

    def get_access_token(self):
        self._fetch_access_token()
        return self._access_token
