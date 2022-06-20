import requests, json

version = 'v9'
endpoint = f'https://discord.com/api/{version}'

def discord_api(endpoint, token, params = {}):
    try:
        r = requests.get(endpoint, params=params)
        return r.json()
    except Exception as e:
        print("The following error occured: ")
        print(e)
        return False