from src.workyoutube import WorkYoutube

class Video(WorkYoutube):
    """
    Класс для получения данных из видео
    """

    def __init__(self, video_id: str):
        # Используем методы из родительского класса для получения данных из видео
        try:
            super().__init__()
            self.video_id = video_id
            super().get_data_on_video_id(self.video_id)
        except:
            self.video_id = video_id

    def __str__(self):
        return f'{self.video_title}'


class PLVideo(WorkYoutube):
    """
    Класс проверяет входит ли видео в плейлист
    """

    def __init__(self, video_id, playlist_id):
        super().__init__()
        super().get_api_key()
        self.playlist_id = playlist_id
        self.video_id = video_id
        # используем методы из родительского метода для получения данных
        self.playlist_videos = super().get_data_on_playlist_videos(self.playlist_id)
        self.list_videos_in_pl = super().list_videos_pl(self.playlist_videos)
        self.get_attrib_video_in_pl()
        self.get_attrib_in_video(super().get_data_on_video_id(self.video_id))

    def get_attrib_video_in_pl(self):
        """
        Функция проверяет входит ли видео в плейлист
        иначе выдаёт исключение
        """
        for video in self.list_videos_in_pl:
            if video == self.video_id:
                return self.video_id
            else:
                raise 'Такого видео нет в плейлисте'

    def __str__(self):
        return f'{self.video_title}'
