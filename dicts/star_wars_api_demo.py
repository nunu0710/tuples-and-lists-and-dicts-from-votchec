# In order to install requests: pip install requests
import requests

response = requests.get("https://swapi.dev/api/films/3")

response_dict = response.json()

print(response_dict)

response_dict.pop("opening_crawl")
response_dict.pop('planets')
response_dict.pop('starships')
response_dict.pop('vehicles')
response_dict.pop('species')
response_dict.pop('url')
response_dict.pop('characters')
print(response_dict)