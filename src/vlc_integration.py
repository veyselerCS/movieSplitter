import os
import vlc
from pathlib import Path

if __name__ == '__main__':
    Instance = vlc.Instance()
    player = Instance.media_player_new()
    path = Path(os.getcwd())
    Media = Instance.media_new(str(path) + '/test/test1.mp4')
    Media.get_mrl()
    player.set_media(Media)
    while True :
        player.play()
