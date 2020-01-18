import requests

params = {"?#q": "pizza"}
r = requests.get("https://google.com", params=params)
print("Status:", r.status_code)

f = open("./page.html", "w+")
f.write(r.text)

