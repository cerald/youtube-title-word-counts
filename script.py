import os
import google.auth
from googleapiclient.discovery import build 
from collections import Counter
import json
from google.oauth2.service_account import Credentials

creds_file = "path/to/credentials.json"
creds_path = os.path.join(os.path.dirname(__file__), creds_file)
with open(creds_path) as f:
    creds_data = json.load(f)
creds = Credentials.from_service_account_info(creds_data)

youtube = build('youtube', 'v3', credentials=creds)

channel_id = input("Enter the channel ID you want to analyze: ")

channel_response = youtube.channels().list(part='contentDetails,snippet', id=channel_id).execute()
playlist_id = channel_response['items'][0]['contentDetails']['relatedPlaylists']['uploads']

word_counts = Counter()
next_page_token = None
while True: 
    playlist_items_response = youtube.playlistItems().list(
        part='snippet',
        playlistId=playlist_id,
        maxResults=50,
        pageToken=next_page_token
    ).execute()
    
    for item in playlist_items_response['items']:
        video_title = item['snippet']['title']
        words = video_title.split()
        for word in words: 
            word_counts[word.lower()] += 1

    next_page_token = playlist_items_response.get('nextPageToken')
    if not next_page_token:
        break

for word, count in word_counts.most_common(10):
    print(f"{word}: {count}")
