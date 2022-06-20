import requests, json, os
from api import discord_api

if not os.path.exists(".token"):
    print("No Authorization Token Found!")
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

channels = discord_api("/users/@me/channels", token)

if not channels:
    print("Unable to contact Discord API")
    print("Please make sure you Authorization Token is correct")
    exit(0)

user_id = input("Enter the Username of the chat you want to download: ")

def DownloadChat():
    pass