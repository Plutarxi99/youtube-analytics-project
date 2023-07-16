import json
import os

# необходимо установить через: pip install google-api-python-client
from googleapiclient.discovery import build

import isodate


# YT_API_KEY скопирован из гугла и вставлен в переменные окружения
#api_key: str = os.getenv('YT_API_KEY')
api_key = 'AIzaSyBERx7q1KhghTEAjZXpz9XKozsRdmdzetM'

# создать специальный объект для работы с API
youtube = build('youtube', 'v3', developerKey=api_key)

print(youtube)

api_key: str = os.getenv('YT_API_KEY')
youtube = build('youtube', 'v3', developerKey=api_key)
channel = youtube.channels().list(id='UC-OVMPlMA3-YCIeg4z5z23A',
                                      part='snippet,statistics').execute()
q_ = json.dumps(channel, indent=2, ensure_ascii=False)


video_title: str = channel['items'][0]['snippet']['title']
video_description: str = channel['items'][0]['snippet']['description']
#video_url: str = channel
subscriber_count: int = channel["items"][0]["statistics"]["subscriberCount"]
video_count: int = channel["items"][0]["statistics"]["videoCount"]
view_count: int = channel['items'][0]['statistics']['viewCount']
print(video_title)
print(video_description)
print(subscriber_count)
print(video_count)
print(view_count)
q = video_title, video_description, subscriber_count, video_count, view_count
with open('moscowpython.json', 'w') as f:
    json.dump(q, f, indent=4)