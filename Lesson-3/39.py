import requests
from requests.exceptions import InvalidURL

try:
    response = requests.get("t34tttertrte")
except InvalidURL:
    print("Invalid url was given")
