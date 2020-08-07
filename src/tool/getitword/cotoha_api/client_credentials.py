import os
import json
from .errors import CotohaApiError


CLIENT_CREDENTIALS = None
CLIENT_CREDENTIALS_PATH = None
DEFAULT_PATH = client_credentials_path = os.path.join(
    os.path.dirname(os.path.abspath(__file__)), "client_credentials.json"
)


class ClientCredentials(object):
    def __init__(self, grant_type, client_id, client_secret):
        self.grant_type = grant_type
        self.client_id = client_id
        self.client_secret = client_secret

    def to_dict(self):
        return {
            "grantType": self.grant_type,
            "clientId": self.client_id,
            "clientSecret": self.client_secret,
        }


def load_client_credentials(path=None):
    global CLIENT_CREDENTIALS
    global CLIENT_CREDENTIALS_PATH

    if CLIENT_CREDENTIALS is not None and CLIENT_CREDENTIALS_PATH == path:
        return

    if path is not None:
        CLIENT_CREDENTIALS_PATH = path
    else:
        CLIENT_CREDENTIALS_PATH = DEFAULT_PATH

    try:
        data = json.loads(open(CLIENT_CREDENTIALS_PATH, "r").read())
        CLIENT_CREDENTIALS = ClientCredentials(
            data.get("grantType"), data.get("clientId"), data.get("clientSecret")
        )
    except Exception as e:
        CLIENT_CREDENTIALS_PATH = None
        CLIENT_CREDENTIALS = None
        raise CotohaApiError(e)


def get_client_credentials(path=None):
    global CLIENT_CREDENTIALS

    load_client_credentials(path)

    if CLIENT_CREDENTIALS is None:
        raise CotohaApiError("client credentials is not exists.")

    return CLIENT_CREDENTIALS
