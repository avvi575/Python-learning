# ============================================================
# CS50P Week 4 — Topic 6: APIs and the requests Library
# ============================================================
# An API (Application Programming Interface) lets your program
# talk to another service over the internet.
#
# requests — the most popular Python HTTP library
#   pip install requests
#
# JSON (JavaScript Object Notation) — a text format for
# exchanging data between programs. Python can convert
# JSON directly into dicts and lists.
#
# Run this file:
#   python3 itunes.py weezer
#   python3 itunes.py "taylor swift"
# ============================================================

import sys
import json

# -------------------------------------------------------
# Validate command-line argument
# -------------------------------------------------------
if len(sys.argv) != 2:
    sys.exit("Usage: python3 itunes.py <search_term>")

search_term = sys.argv[1]

# -------------------------------------------------------
# Import requests (third-party — pip install requests)
# -------------------------------------------------------
try:
    import requests
except ImportError:
    sys.exit("requests not installed. Run: pip install requests")

# -------------------------------------------------------
# Make the API call
# requests.get(url) sends an HTTP GET request and returns
# a Response object.
# -------------------------------------------------------
print(f"Searching iTunes for: '{search_term}'")
print("-" * 40)

url = f"https://itunes.apple.com/search?entity=song&limit=10&term={search_term}"
response = requests.get(url)

# -------------------------------------------------------
# response.json() converts the JSON text into a Python dict
# json.dumps(obj, indent=2) formats it nicely for printing
# -------------------------------------------------------
data = response.json()

# Print raw pretty-printed JSON (optional — comment out to reduce noise)
# print(json.dumps(data, indent=2))

# -------------------------------------------------------
# Extract just the track names from the results list
# data["results"] → list of song dicts
# each song dict has keys like "trackName", "artistName", etc.
# -------------------------------------------------------
print(f"Top songs:\n")
for i, result in enumerate(data["results"], start=1):
    track  = result.get("trackName", "Unknown Track")
    artist = result.get("artistName", "Unknown Artist")
    print(f"  {i:2}. {track} — {artist}")

# -------------------------------------------------------
# Bonus: show one full result dict to understand the structure
# -------------------------------------------------------
if data["results"]:
    print("\n=== Full JSON for first result (pretty-printed) ===")
    print(json.dumps(data["results"][0], indent=2))

# -------------------------------------------------------
# Key concepts:
#
#   requests.get(url)     → sends HTTP GET, returns Response
#   response.json()       → parses JSON body → Python dict/list
#   json.dumps(obj, indent=2) → pretty-print any dict/list
#   response.status_code  → HTTP status (200 = OK, 404 = Not Found)
# -------------------------------------------------------
