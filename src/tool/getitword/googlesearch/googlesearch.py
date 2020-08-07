from splash import Splash
from urllib import parse
from bs4 import BeautifulSoup

SEARCH_URL = "https://www.google.co.jp/search"


class GoogleSearch(object):
    def __init__(self):
        pass

    def create_search_url(self, keyword, start=0, num=100, filter="0"):
        return (
            SEARCH_URL
            + "?"
            + parse.urlencode(
                {"q": keyword, "start": start, "num": num, "filter": filter,}
            )
        )

    def search(self, keyword, start=0, num=20):
        query = self.create_search_url(keyword, start=start, num=num)
        return Splash.get(query)

    def search_links(self, keyword, start=0, num=20):
        result = self.search(keyword, start=start, num=num)
        soup = BeautifulSoup(result.content, "lxml")
        elements = soup.select(".rc > .r > a")
        links = [e.get("href") for e in elements]
        return [l for l in links if l]
