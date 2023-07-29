import datetime

from workyoutube_lat_del import WorkYoutube


class PlayList(WorkYoutube):

    def __init__(self, playlist_id):
        super().__init__()
        self.playlist_id = playlist_id
        self.title = super().get_pl_title(self.playlist_id)
        self.url = super().get_pl_url(self.playlist_id)
        self.object_pl = super().get_object_video_in_playlist(self.playlist_id)

    @property
    def total_duration(self):
        """
        возвращает объект класса `datetime.timedelta` с суммарной длительность
        плейлиста (обращение как к свойству, использовать `@property`)
        @return:
        """
        q = datetime.timedelta(seconds=0)
        a = super().get_time_in_video(self.object_pl)
        for x in a:
            q += x
        return q

    def show_best_video(self):
        """
        возвращает ссылку на самое популярное видео из плейлиста
        (по количеству лайков)
        @return:
        """
        max_like = []
        dict_like_url = super().get_pl_like(self.playlist_id)
        for k, v in dict_like_url.items():
            max_like.append(k)
        return dict_like_url[max(max_like)]
