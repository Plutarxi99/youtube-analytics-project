import json
import os

import isodate
from googleapiclient.discovery import build


class WorkYoutube:
    """
    Класс для избежания повторений кода
    И использования его в качестве базового класс
    """

    def __init__(self):
        self.video_like_count = None  # количество лайков
        self.video_url = None  # ссылка на видео
        self.video_view_count = None  # количество просмотров
        self.video_title = None  # название видео
        self.video_id = None  # id видео

    def get_data_on_video_id(self, video_id):
        """
        @param video_id: id видео
        @return: объект для извлечения данных из видео
        """
        video_response = self.get_api_key().videos().list(part='snippet,statistics,contentDetails,topicDetails',
                                                          id=video_id
                                                          ).execute()
        return video_response

    def get_data_on_playlist_videos(self, playlist_id):
        """
        @param playlist_id: id плейлиста
        @return: объект для работы с плейлистом
        """
        playlist_videos = self.get_api_key().playlists().list(
            part="snippet",
            id=playlist_id,
            maxResults=50
        ).execute()
        return playlist_videos

    def get_attrib_in_video(self, video_response):
        """
        Функция для получения атрибутов из видео:

            Выводит:
                video_title - название видео
                video_url - ссылка на видео
                video_view_count - количество просмотров
                video_like_count - количество лайков
        @param video_response: объект для работы с плейлистом
        """
        self.video_title = \
            video_response['items'][0]['snippet']['title']

        self.video_url = \
            f"https://www.youtube.com/watch?v={self.video_id}"

        self.video_view_count = \
            video_response['items'][0]['statistics']['viewCount']

        self.video_like_count = \
            video_response['items'][0]['statistics']['likeCount']

    def get_playlist_videos(self, playlist_id):
        playlist_videos = self.get_api_key().playlistItems().list(playlistId=playlist_id,
                                                       part='contentDetails',
                                                       maxResults=50,
                                                       ).execute()
        return playlist_videos
    def get_object_video_in_playlist(self, playlist_id):
        """
        Получение объекта из плэйлиста состоящего из аттрибутов видео и последующей работы с ним
        @return: объект для работы с плэйлистами
        """
        video_response = self.get_api_key().videos().list(part='contentDetails,statistics',
                                                          id=','.join([video['contentDetails']['videoId'] for video in
                                                                       self.get_playlist_videos(playlist_id)[
                                                                           'items']])
                                                          ).execute()
        return video_response

    def get_time_in_video(self, video_response_pl):
        """
        вывести длительности видеороликов из плейлиста
        @param video_response_pl: объект для работы с плэйлистами
        @return:
        """
        list_time_video_in_pl = []
        for video in video_response_pl['items']:
            # YouTube video duration is in ISO 8601 format
            iso_8601_duration = video['contentDetails']['duration']
            duration = isodate.parse_duration(iso_8601_duration)
            list_time_video_in_pl.append(duration)
        return list_time_video_in_pl

    def get_pl_title(self, id_playlist):
        """
        Получение названия плейлиста
        @param id_playlist:id_playlist
        @return: title playlist
        """
        a = self.get_data_on_playlist_videos(id_playlist)
        return a["items"][0]["snippet"]["title"]

    def get_pl_url(self, id_playlist):
        """
        Получение ссылки плейлиста
        @param id_playlist: id_playlist
        @return: url playlist
        """
        return f'https://www.youtube.com/playlist?list={id_playlist}'

    def get_pl_like(self, id_playlist):
        """
        Получение список видео по лайкам
        @param id_playlist:id_playlist
        @return:
        """
        q = {}
        a = self.get_object_video_in_playlist(id_playlist)
        for x in range(len(a["items"])):
            items = a["items"]
            # q.append(items[x]["statistics"]["likeCount"])
            q[items[x]["statistics"]["likeCount"]] = f'https://youtu.be/{items[x]["id"]}'
        return q
    def printj(self, dict_to_print: dict) -> None:
        """Выводит словарь в json-подобном удобном формате с отступами"""
        print(json.dumps(dict_to_print, indent=2, ensure_ascii=False))

    @staticmethod
    def list_videos_pl(playlist_videos):
        """
        Получение списка видео из плейлиста
        @param playlist_videos: объект для работы с плейлистом
        @return: список из id видео, которые находятся в плейлисте list[video_ids]
        """
        video_ids: list[str] = [video['contentDetails']['videoId'] for video in playlist_videos['items']]
        return video_ids

    @staticmethod
    def get_api_key():
        """
        Функция для получения объекта для дальнейшей работы с API Youtube
        @return:
        """
        api_key: str = os.getenv('YT_API_KEY')
        youtube = build('youtube', 'v3', developerKey=api_key)
        return youtube
