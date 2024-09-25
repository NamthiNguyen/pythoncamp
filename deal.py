import json
import requests
from bs4 import BeautifulSoup

api_url = "https://www.mcdonalds.com/us/en-us/full-menu/5-dollar-meals.html"
auth_key= {
    "Authorization": "API_KEY"
}



respone = requests.get(api_url, headers=auth_key)

if respone.status_code == 200:
    deals = respone.json()

for deal in deals:
    print(f"Deal: {deal['title']} - {deal['description']}")
else:
    print("fail to retrieved data from store")