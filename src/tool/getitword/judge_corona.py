import collections
from pprint import pprint
from gensim.models.doc2vec import Doc2Vec
from corona_api import normalize


label = {
    "ca6140c00a490e24dcc201299e015c322bf680c0616834b4aef933929473a9db": "beer",
    "bf1503af01cf59cda48d52f53ef236b730923ee1877d5c956bba3b2427f35bc5": "virus",
    "2c2079dc496373bb57bc9dfc3b86aee5acb9d626f68c8547032c1ded68684989": "suns"
}


def main():
    model = Doc2Vec.load(f"/code/data/corona.model")

    judge(model, "コロナビールを飲んだら美味しい")
    judge(model, "新型コロナウイルスに怯えている")
    judge(model, "太陽から発せられるコロナの温度は高温")
    

def judge(model, word):
    print(f"judge: {word}")
    words = normalize(word).split()
    x = model.infer_vector(words)
    most_similar_texts = model.docvecs.most_similar([x])
    count = collections.Counter(
        [
            label.get(similar_text[0].split("-")[0])
            for similar_text in most_similar_texts
        ]
    )

    pprint(count)

