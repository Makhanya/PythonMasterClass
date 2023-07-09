import requests
url = "https://www.google.com/"
response = requests.get(url)

# status code 200
print(f"Your request to {url} came back w/ status code {response.status_code}")
