import sys
sys.path.insert(0, '/Users/mamang/Library/CloudStorage/OneDrive-Personal/Tools/API')
sys.path.insert(0, r'C:\Users\nguye\OneDrive\Tools\API')

import info
import syllabus
from video import get_tittle
from pytube import Playlist

school = info.Domain('khl', 'khl')
iid_syllabus = 7526001
url_playlist = 'https://www.youtube.com/watch?v=thOMBzE8wWQ&list=PLpeoU1to5k6_BXMzFTDV3TGFeygC9c83s'
pls = Playlist(url_playlist)
video = []
for item in pls:
    video.append({
        'name': get_tittle(item),
        'id':item
    })
content = []
for v in video:
    content.append(syllabus.add_video_youtube(school, iid_syllabus, v))
syllabus.update(school, iid_syllabus, content)