import argparse
import time
from typing import List
from pprint import pprint
from extract_text_service import TextExtractService
from cotoha_api import CotohaApiService, get_client_credentials


def setup_argparse():
    parser = argparse.ArgumentParser()
    parser.add_argument("--urls", nargs="*")
    parser.add_argument("--filepath")
    return parser


def get_it_words(urls: List[str]):
    client_credentials = get_client_credentials()
    api_service = CotohaApiService(client_credentials)
    service = TextExtractService()

    words = []
    datas = []
    for url in urls:
        # 短期間でのリクエストを避ける
        time.sleep(1)

        text = service.get_text_from_url(url)

        try:
            result = api_service.get_keyword(text)
        except Exception as e:
            print(e)
            continue

        for obj in result.result.objects:
            words.append(obj.form)

    return words


def load_file(filepath: str):
    with open(filepath, "r") as f:
        return f.read().split("\n")


def get_urls_from_args(args):
    urls = args.urls
    filepath = args.filepath

    result = []
    if filepath:
        result.extend(load_file(filepath))

    if isinstance(urls, list):
        result.extend(urls)

    if not result:
        raise Exception("url is not")

    return result


def main():
    parser = setup_argparse()
    args = parser.parse_args()
    urls = get_urls_from_args(args)
    words = get_it_words(urls)
    pprint(words)
