"""
    What's a Query String?
    
        *A way to pass data to the server as part of a GET request
        *http://www.example.com/?key1=value1&key2=value2

"""
import requests
url = "https://icanhazdadjoke.com/search"

response = requests.get(
    url,
    headers={"Accept": "application/json"},
    params={"term": "cat", "limit": 1}
)
data = response.json()

# print(data["joke"])
# print(f"status: {data['status']}")

print(data["results"])
