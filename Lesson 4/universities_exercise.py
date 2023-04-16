import requests

url = "http://universities.hipolabs.com/search?country=israel"
response = requests.get(url)
if response.status_code == 200:
    universities = response.json()
    assert len(universities) >= 5
    print(len(universities))
