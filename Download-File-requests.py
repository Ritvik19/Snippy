import requests

res = requests.get("file/url")
res.raise_for_status()
with open("file.txt", "wb") as f:
    for chunk in res.iter_content(100000):
        f.write(chunk)
