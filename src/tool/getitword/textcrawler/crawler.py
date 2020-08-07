import re
import requests
from bs4 import BeautifulSoup
from splash import Splash

exclude_classname = re.compile("header", re.IGNORECASE)
exclude_tags = [
    "script",
    "style",
    "header",
    "footer",
    "iframe",
    "meta",
    "noscript",
    "a",
    "pre",
    "select",
    "option",
    "input",
    "title",
]


def remove_exclude_tags(soup):
    for tag in soup(exclude_tags):
        tag.decompose()

    for tag in soup.find_all(class_=exclude_classname):
        tag.decompose()


class TextCrawler(object):
    def get_text(self, url):
        response = Splash.get(url)
        if response.headers.get('content-type') == "pplication/json":
            r = json.loads(response.content)
            error = r.get("error")
            if error:
                raise Exception(error)

        soup = BeautifulSoup(response.content, "html.parser")
        remove_exclude_tags(soup)
        return soup.get_text()
