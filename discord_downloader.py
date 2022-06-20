import os, json
from time import sleep
from api import discord_api

if not os.path.exists("data"):
    os.mkdir("data")

if not os.path.exists(".token"):
    print("No Authorization Token Found!")
    print("See README.md for how to find your authorization token")
    token = input("Enter Authorization Token: ")

    with open(".token", "w+") as f:
        f.write(token)
        f.close()
    
    print("The token has been saved in the current directory.")
    print("Please remember to delete it once you are done using this app.")
else:
    print("Authorization Token Found")
    with open(".token", "r") as f:
        token = f.readline()

print("Retrieving all your channels...")
channels = discord_api("/users/@me/channels", token)

if not channels:
    print("Unable to contact Discord API")
    print("Please make sure you Authorization Token is correct")
    exit(0)

username = ''

while True:
    username = input("Enter Username (or 0 to exit): ")

    if username == '0':
        break

    channel = [c for c in channels if c['recipients'][0]['username'] == username]

    if len(channel) == 0:
        print("User not found! Usernames are case-sensitive.")
    else:
        channel = channel[0]
        channel_id = channel['id']
        file = input(f'Enter save file name ({username}.json by default): ')
        
        if file.strip() == '':
            file = f'{username}.json'
        
        messages = []

        last_message_id = 0
        counter = 0
        i = 0
        while True:
            print(f'Fetching Messages ({counter} total)')

            msgs = discord_api(f'/channels/{channel_id}/messages', token, params={
                'after': last_message_id,
                'limit': 100 # max limit supported by Discord API
            })

            if not msgs:
                print('Error while retrieving messages')
                exit(0)

            ## Rate Limiting Issue

            if "retry_after" in msgs:
                print("Rate limited ... waiting 5 seconds before retrying")
                sleep(5)
            else:
                messages[:0] = msgs
                counter += len(msgs)

                if len(msgs) < 100:
                    break
                else:
                    last_message_id = msgs[0]['id']
        
        ## Save Messages to File
        print(f"Fetched a total of {counter} messages")
        with open(f"data/{file}", 'w+') as f:
            f.write(json.dumps(messages, indent = 2))
            f.close()
        print('Messages Saved!')
