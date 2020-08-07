import requests

SPLASH_API_URL = "http://splash:8050/render.html"


class Splash(object):
    @classmethod
    def get(cls, url, wait=2, api_url=None):
        api_url = api_url if api_url else SPLASH_API_URL
        return requests.get(api_url, params={"url": url, "wait": wait})
