"""
    requests Module
        Lets us make HTTP requests from our Python code!
        Installed using pip
        Useful for web scraping/crawling, grabbing data from other APIs etc
    Request Headers
import requests
response = requests.get(
    "http://www.google.com",
    headers={
        "header1": "value",
        "header2": "values2"
    }
)
        
"""
# import requests
# url = "https://icanhazdadjoke.com"
# response = requests.get(url, headers={"Accept": "application/json"})
# print(response.text)
# print(response.json())

import requests
url = "https://icanhazdadjoke.com"
response = requests.get(url, headers={"Accept": "application/json"})
data = response.json()
print(data["joke"])
