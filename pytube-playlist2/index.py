import re
from pytube import Playlist
from pytube import YouTube

YOUTUBE_STREAM_AUDIO = '140' # modify the value to download a different stream
DOWNLOAD_DIR = 'C:\\xampp\\htdocs\\python\\alpha-test\\music'

url = input('Digite sua url: ')
playlist = Playlist(url)

print('Seu download começou!')
playlist._video_regex = re.compile(r"\"url\":\"(/watch\?v=[\w-]*)")



print(len(playlist.video_urls))

for url in playlist.video_urls:
    print(url)

# physically downloading the audio track
for video in playlist.videos:
    audioStream = video.streams.get_by_itag(YOUTUBE_STREAM_AUDIO)
    audioStream.download(output_path=DOWNLOAD_DIR)

print('DOwnload completo!!!')