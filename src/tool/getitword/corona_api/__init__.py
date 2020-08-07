import json
from pprint import pprint

from gensim.models.doc2vec import Doc2Vec
from gensim.models.doc2vec import TaggedDocument

from .const import DATA_DIR, NEOLOGD_PATH
from .normalize import normalize


def create():
    with open("/code/data/search_result.json", "r") as f:
        search_result = json.loads(f.read())
    
    trainings = []
    t = []
    for r in search_result:
        links = r.get("links")
        word = r.get("word")
        hash_s = r.get("hash")

        texts = []
        for link in links:
            if r.get("success") == 0:
                continue
            text = link.get("text")
            text = normalize(text)
            texts.append(text)
            t.append(text)

        trainings.extend(
            [
                TaggedDocument(words=data.split(), tags=[f"{hash_s}-{i}"])
                for i, data in enumerate(texts)
            ]
        )

    with open("/code/data/normalized.txt", "w") as f:
        f.write("\n".join(t))

    model = Doc2Vec(documents=trainings, dm=0, min_count=1, workers=4)
    model.save(f"/code/data/corona.model")