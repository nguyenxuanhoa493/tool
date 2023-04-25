from pytube import Playlist
import urllib.request
import json
import urllib

def get_tittle(link):
    params = {"format": "json", "url": link}
    url = "https://www.youtube.com/oembed"
    query_string = urllib.parse.urlencode(params)
    url = url + "?" + query_string

    with urllib.request.urlopen(url) as response:
        response_text = response.read()
        data = json.loads(response_text.decode())
    return data['title']

school = info.Domain('mtholding', 'TDMT')
iid_course = 4023763
course.learn_video(school, iid_course, 4310217)