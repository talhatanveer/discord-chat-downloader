import requests, json

version = 'v9'
endpoint = f'https://discord.com/api/{version}'

def discord_api(path, token, params = {}):
    try:
        r = requests.get(f'{endpoint}{path}', params=params, headers={
            'Authorization':token
        })
        return r.json()
    except Exception as e:
        print("The following error occured: ")
        print(e)
        return False