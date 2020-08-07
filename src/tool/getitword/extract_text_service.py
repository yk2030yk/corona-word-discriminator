import re
import requests
from bs4 import BeautifulSoup

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
]


def get_html(url: str):
    response = requests.get(url)
    return response.content


def remove_exclude_tags(soup):
    for tag in soup(exclude_tags):
        tag.decompose()

    for tag in soup.find_all(class_=exclude_classname):
        tag.decompose()


def normalize_text(text: str):
    return re.sub(r"[ | ]", "", text)


class TextExtractService(object):
    def get_text_from_url(self, url: str):
        html = get_html(url)
        soup = BeautifulSoup(html, "lxml")
        remove_exclude_tags(soup)
        text = soup.get_text()
        return normalize_text(text)
