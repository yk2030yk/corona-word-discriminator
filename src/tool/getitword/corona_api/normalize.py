import re
import neologdn
import MeCab
import emoji

wakati_split = " "
stop_words = open(f"/code/getitword/corona_api/stopwords.txt", "r").read().split("\n")


def _normalize_neologdn(text):
    return neologdn.normalize(text)


def _normalize_remove(text):
    return text.replace("\n", "")


def _normalize_lower(text):
    return text.lower()


def _normalize_remove_emoji(text):
    return "".join([c for c in text if c not in emoji.UNICODE_EMOJI])


def _normalize_remove_stop_words(split_words):
    return [word for word in split_words if word not in stop_words]


def _normalize_number(text):
    text = re.sub(r'(\d)([,.])(\d+)', r'\1\3', text)
    text = re.sub(r'\d+', '0', text)
    return text


def _normalize_kigou(text):
    text = re.sub(r'[!-/:-@[-`{-~「」（）『』]', r' ', text)
    text = re.sub(u'[■-♯]', ' ', text)
    return text


def _split_wakati_to_words(text):
    return text.split(wakati_split)


def _join_words_to_wakati(words):
    return wakati_split.join(words)


def normalize(text):
    tagger = MeCab.Tagger("-O wakati")

    t = text
    t = _normalize_neologdn(t)
    t = _normalize_lower(t)
    t = _normalize_remove_emoji(t)
    # t = _normalize_number(t)
    t = _normalize_kigou(t)
    t = _normalize_remove(t)

    wakati = tagger.parse(t)
    words = _split_wakati_to_words(wakati)
    words = _normalize_remove_stop_words(words)

    return _join_words_to_wakati(words)
