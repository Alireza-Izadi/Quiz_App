import requests

#---------------------REQUEST API----------------------#
response = requests.get("https://opentdb.com/api.php?amount=50&type=boolean")
response.raise_for_status()
data = response.json()
questions = data["results"]