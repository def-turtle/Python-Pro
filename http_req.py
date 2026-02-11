import requests

params1 = {
    "q": "python",
    "limit": 5
}

response = requests.get("https://github.com/settings/security", params=params1)

print(response.url)   # See full URL with params
print(response.json())  # Parse JSON response
