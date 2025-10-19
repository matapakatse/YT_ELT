import requests # Library to make HTTP requests
import json  # Library to work with JSON data

import os    # Library to work with environment variables
from dotenv import load_dotenv  # Library to load environment variables from a .env file

load_dotenv(dotenv_path="./.env")  # Load variables from .env file

API_KEY = os.getenv("API_KEY")  

# The channel handle for which you want data
CHANNEL_HANDLE = "MrBeast"

def get_playlist_id():
    try:

        # Construct the API URL
        # f-strings let us insert variables directly into the string
        url = f"https://youtube.googleapis.com/youtube/v3/channels?part=contentDetails&forHandle={CHANNEL_HANDLE}&key={API_KEY}"

        # Send a GET request to the URL
        response = requests.get(url)

        
        response.raise_for_status()

        # Convert the response from JSON into a Python dictionary
        data = response.json()

        # Print the JSON in a readable, indented format
        # Helps us understand the structure of the data
        print(json.dumps (data, indent=4))

        # Get the first item from the 'items' list in the JSON (contains the channel details)
        channel_items = data['items'][0]
        
        # Navigate through contentDetails -> relatedPlaylists -> uploads
        # This gives us the uploads playlist ID of the channel
        channel_playslist_id = channel_items['contentDetails']['relatedPlaylists']['uploads']

            
        # Print the uploads playlist ID
        #print(channel_playslist_id)

        return channel_playslist_id

    except requests.exceptions.RequestException as e:
        raise e
if __name__ == "__main__":
    get_playlist_id()


