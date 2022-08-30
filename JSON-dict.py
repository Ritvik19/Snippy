import json

with open("model.json", "w") as f:
    k = model.keys()
    v = model.values()
    k1 = [str(i) for i in k]
    json.dump(json.dumps(dict(zip(*[k1, v]))), f)


with open("model.json", "r") as f:
    data = json.load(f)
    dic = json.loads(data)
    k = dic.keys()
    v = dic.values()
    k1 = [eval(i) for i in k]
    model = dict(zip(*[k1, v]))
