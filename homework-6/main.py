# from src.video import Video
import sys
sys.path.append('/home/egor/PycharmProjects/clone_desktot/OOP/youtube-analytics-project')
from src.video import Video

if __name__ == '__main__':
    broken_video = Video('broken_video_id')
    assert broken_video.video_title is None
    assert broken_video.video_like_count is None
