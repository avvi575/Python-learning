# 06 — APIs & the `requests` Library

## What is an API?

An **API** (Application Programming Interface) lets your program request data from another service over the internet. You send a URL, they send back data — usually in **JSON** format.

## Install

```bash
pip install requests
```

## Basic pattern

```python
import requests
import json

response = requests.get("https://some-api.com/endpoint?param=value")
data = response.json()          # JSON → Python dict/list
print(json.dumps(data, indent=2))  # pretty-print
```

## iTunes API example

```bash
python3 itunes.py weezer
python3 itunes.py "taylor swift"
```

```python
url = "https://itunes.apple.com/search?entity=song&limit=10&term=weezer"
response = requests.get(url)
data = response.json()

for result in data["results"]:
    print(result["trackName"])
```

## JSON in Python

JSON text is automatically converted to Python types:

| JSON | Python |
|------|--------|
| `{}` | `dict` |
| `[]` | `list` |
| `"text"` | `str` |
| `123` | `int` |
| `true/false` | `True/False` |
| `null` | `None` |

## Useful response attributes

```python
response.status_code   # 200 = OK, 404 = not found
response.json()        # parse JSON body
response.text          # raw text body
```
