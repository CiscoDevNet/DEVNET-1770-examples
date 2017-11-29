import requests


def get_joke():
    r = requests.get('https://api.chucknorris.io/jokes/random?category=science')
    return r.json()

def get_joke_text():
    r = requests.get('https://api.chucknorris.io/jokes/random?category=science')
    return r.text

def joke_length():
    joke = get_joke()
    return len( joke["value"] )