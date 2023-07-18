import json
import os

from googleapiclient.discovery import build


class Channel:
    """Класс для ютуб-канала"""

    def __init__(self, channel_id: str) -> None:
        """Экземпляр инициализируется id канала. Дальше все данные будут подтягиваться по API."""
        self.custom_url = None
        self.__channel_id = channel_id
        self.title = None
        self.video_description = None
        self.url = None
        self.subscriber_count = None
        self.video_count = None
        self.view_count = None

    def __str__(self):
        """
        Для отображения информации об объекте класса для пользователей
        """
        return f'{self.title} ({self.url})'

    def __add__(self, other):
        """
        Позволяет прибавлять к экземпляру класса количество подписчиков (subscriber_count)
        """
        return int(self.subscriber_count) + int(other.subscriber_count)

    def __sub__(self, other):
        """
        Позволяет вычитать к экземпляру класса количество подписчиков (subscriber_count)
        """
        return int(self.subscriber_count) - int(other.subscriber_count)

    def __gt__(self, other):
        """
        Позволяет сравнивать экземпляры классов по количеству подписчиков (subscriber_count)
        """
        return self.subscriber_count > other.subscriber_count

    def __ge__(self, other):
        """
        Позволяет сравнивать экземпляры классов по количеству подписчиков (subscriber_count)
        """
        return self.subscriber_count >= other.subscriber_count

    def __lt__(self, other):
        """
        Позволяет сравнивать экземпляры классов по количеству подписчиков (subscriber_count)
        """
        return self.subscriber_count < other.subscriber_count

    def __le__(self, other):
        """
        Позволяет сравнивать экземпляры классов по количеству подписчиков (subscriber_count)
        """
        return self.subscriber_count <= other.subscriber_count

    def __eq__(self, other):
        """
        Позволяет сравнивать экземпляры классов по количеству подписчиков (subscriber_count)
        """
        return self.subscriber_count == other.subscriber_count

    def print_info(self) -> None:
        """Выводит в консоль информацию о канале."""
        api_key: str = os.getenv('YT_API_KEY')
        youtube = build('youtube', 'v3', developerKey=api_key)
        channel = youtube.channels().list(id=self.__channel_id, part='snippet,statistics').execute()
        print(json.dumps(channel, indent=2, ensure_ascii=False))

    def get_service(self):
        """
        Возвращающий объект для работы с YouTube API
        """
        api_key: str = os.getenv('YT_API_KEY')
        youtube = build('youtube', 'v3', developerKey=api_key)

        return youtube

    def to_json(self, data: '') -> '':
        """
        Cохраняющий в файл значения атрибутов экземпляра Channel
        """
        # Создаём словарь для более корректного отображания
        searching_data = {
            'channel_id': self.__channel_id,
            'title': self.title,
            'description': self.video_description,
            'url': self.url,
            'subscriber_count': self.subscriber_count,
            'video_count': self.video_count,
            'view_count': self.view_count
        }
        # Делаем запись в json формате в файл указанной функции data
        with open(data, "w") as file:
            # Записываем данные в файл JSON
            json.dump(searching_data, file, indent=2, ensure_ascii=False)

    def get_attribut(self):
        """
        Для отображения вызываемых атрибутов youtube-канала
        """
        channel = self.get_service().channels().list(id=self.__channel_id, part='snippet,statistics').execute()
        # Сокращаем строки кода путем сохранения паттерна в вызове объекта
        items = channel['items'][0]

        # Обращаемся к нужным параметрам youtube-канала
        self.title: str = items['snippet']['title']
        self.video_description: str = items['snippet']['description']
        self.custom_url = items['snippet']['customUrl']
        self.url = f"https://www.youtube.com/{self.custom_url}"
        self.subscriber_count: int = items["statistics"]["subscriberCount"]
        self.video_count: int = items["statistics"]["videoCount"]
        self.view_count: int = items['statistics']['viewCount']
