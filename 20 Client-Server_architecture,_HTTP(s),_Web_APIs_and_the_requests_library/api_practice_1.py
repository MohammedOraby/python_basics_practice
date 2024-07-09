import requests 

response = requests.get("http://api.aladhan.com/v1/timingsByCity?city=London&country=GB")
timings = response.json()["data"]["timings"]
print(timings)
