from textcrawler import TextCrawler
from googlesearch import GoogleSearch
from pprint import pprint
import hashlib
import json
import re

data_dir = "/code/data/"
search_result_json = f"{data_dir}/search_result.json"


def main():
    text_crawler = TextCrawler()
    google_search = GoogleSearch()

    search_words = ["コロナ　ビール", "コロナ　ウイルス", "コロナ　太陽"]

    search_result = []
    for word in search_words:
        print("start 「{word}」")
        word_hash = hashlib.sha256(word.encode("utf-8")).hexdigest()

        links_results = []
        links = google_search.search_links(word, num=40)
        for link in links:
            print(f"getting ... {link}")
            
            try:
                text = text_crawler.get_text(link)
                text = normalize(text)

                links_results.append(
                    {"url": link, "success": 1, "text": text, "reason": None}
                )
            except Exception as e:
                links_results.append(
                    {"url": link, "success": 0, "text": None, "reason": e}
                )

        search_result.append({"word": word, "hash": word_hash, "links": links_results})

    with open(search_result_json, "w") as f:
        f.write(json.dumps(search_result, indent=4, ensure_ascii=False))

    print("finish to output search result.")


def normalize(text):
    text = re.sub("[\t　]", " ", text)
    text = re.sub("\r\n", "\n", text)
    text = re.sub("\s+", " ", text)
    text = re.sub("\n+", "\n", text)

    return text