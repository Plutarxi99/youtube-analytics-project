from video_l_d import Video

if __name__ == '__main__':
    broken_video = Video('broken_video_id')
    assert broken_video.video_title is None
    assert broken_video.video_like_count is None
