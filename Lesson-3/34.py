import requests


def check_if_url_up(url):
    response = requests.get(url)
    if 200 <= response.status_code < 300:  # ddd
        return True
    else:
        return False


print(check_if_url_up("https://api.github.com"))
print("Hello")
