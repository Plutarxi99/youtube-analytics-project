import json
import os

from googleapiclient.discovery import build


class Channel:
    """Класс для ютуб-канала"""

    def __init__(self, channel_id: str) -> None:
        """Экземпляр инициализируется id канала. Дальше все данные будут подтягиваться по API."""
        self._channel_id = channel_id
        self.title = None
        self.video_description = None
        self.url = None
        self.subscriber_count = None
        self.video_count = None
        self.view_count = None

    def print_info(self) -> None:
        """Выводит в консоль информацию о канале."""
        api_key: str = os.getenv('YT_API_KEY')
        youtube = build('youtube', 'v3', developerKey=api_key)
        channel = youtube.channels().list(id=self._channel_id, part='snippet,statistics').execute()
        print(json.dumps(channel, indent=2, ensure_ascii=False))

    def get_service(self):
        """
        возвращающий объект для работы с YouTube API
        """
        api_key: str = os.getenv('YT_API_KEY')
        youtube = build('youtube', 'v3', developerKey=api_key)

        return youtube

    def to_json(self, data: '') -> '':
        """
        сохраняющий в файл значения атрибутов экземпляра Channel
        """

        with open(data, 'w') as f:
            json.dump(f'''{self.title},
                      {self.video_description},
                      {self.subscriber_count},
                      {self.view_count},
                      {self.view_count}''',
                      f, indent=4)

    def get_attribut(self):
        channel = self.get_service().channels().list(id=self._channel_id, part='snippet,statistics').execute()

        items = channel['items'][0]

        self.title: str = items['snippet']['title']
        self.video_description: str = items['snippet']['description']
        # url: str = channel
        self.subscriber_count: int = items["statistics"]["subscriberCount"]
        self.video_count: int = items["statistics"]["videoCount"]
        self.view_count: int = items['statistics']['viewCount']
