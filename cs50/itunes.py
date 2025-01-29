import json
# https://pypi.org/project/requests/
import requests
import sys

if len(sys.argv) !=2:
    sys.exit()

response = requests.get("https://itunes.apple.com/search?entity=song&limit=15&term=" + sys.argv[1])


o = response.json()
for result in o["results"]:
    print(f"result: {result["trackName"]}")

# print(json.dumps(response.json(), indent=2))

