# discord-chat-downloader
Save your Discord chats as JSON files

## Usage
`python3 discord_downloader.py`

The app will store your Authorization token in a `.token` file. You
may delete this token or keep it, just keep in mind that it's there so that
in case the API requests don't go through, it might be because the token
has expired.

## Getting the Authorization Token
#### Step 1: Login to Discord via Web Browser
#### Step 2: Open the Discord Web App
#### Step 3: Open the Developer Console ("Inspect Element")
#### Step 4: Click on "Network" / "Requests", etc depending on your browser
#### Step 5: Filter by "XHR/Fetch"
#### Step 6: Click on any network request (if there are none, hit reload)
#### Step 7: Under "Request Headers", there should be a field called "Authorization", just copy its value

This goes without saying but please do not share this token with anyone, it can be used to access all data on your Discord account as well as send messages (or anything else you are able to do with the
Discord app)