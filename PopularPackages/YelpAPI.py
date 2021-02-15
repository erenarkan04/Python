import requests
import config
url = "https://api.yelp.com/v3/businesses/search"

header = {
    "Authorization": "Bearer " + config.api_key
}

params = {
    "term": "bakery",
    "location": "11238"

}
response = requests.get(url, headers=header, params=params)

businesses = response.json()["businesses"]
print(businesses)

for business in businesses:
    print(business["name"])

businesses2 = [business["name"] for business in businesses if business["rating"] > 4]

print(businesses2)
