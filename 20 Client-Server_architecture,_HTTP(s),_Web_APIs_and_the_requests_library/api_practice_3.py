import requests

# fitch a specific joe by id
response = requests.get("https://icanhazdadjoke.com//j/Qn31o49Musc",headers={"Accept":"application/json"},)

print(response.json())