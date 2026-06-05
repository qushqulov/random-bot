import requests

def get_random_dog():
    try:
        response = requests.get("https://dog.ceo/api/breeds/image/random").json()
        return response["message"]
    except Exception:
        return None

def get_random_cat():
    try:
        response = requests.get("https://api.thecatapi.com/v1/images/search").json()
        return response[0]["url"]
    except Exception:
        return None