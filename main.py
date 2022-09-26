from tkinter import *

from pytube import YouTube
import os



escolha = int(input('Escolha o metodo de download: '))

if escolha == 1:
    url = input('Digite o link do vídeo \n >>')
    youTube = YouTube(url)
    print('iniciando')
    print("Titulo: " + youTube.title)
    video = youTube.streams.get_highest_resolution()
    video.download('C:\\xampp\\htdocs\\python\\Final_test\\music')
    print('Download concluido!!!')
elif escolha == 2:
    import re
    from pytube import Playlist
    from pytube import YouTube

    YOUTUBE_STREAM_AUDIO: str = '140'  # modify the value to download a different stream
    DOWNLOAD_DIR = 'C:\\xampp\\htdocs\\python\\Final_test\\music'

    url = input('Digite sua playlist \n >>')
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

    print('Download completo!!!')

elif escolha == 3:
    DOWNLOAD_DIR = 'C:\\xampp\\htdocs\\python\\Final_test\\music'
    # url input from user
    yt = YouTube(
        str(input('Digite seu link: \n>> ')))
    print('Seu download começou!')
    # extract only audio
    video = yt.streams.filter(only_audio=True).first()

    # download the file
    out_file = video.download(output_path=DOWNLOAD_DIR)
    
    # save the file
    base, ext = os.path.splitext(out_file)
    new_file = base + '.mp3'
    os.rename(out_file, new_file)
    
    # result of success
    print(yt.title + " \nSeu download foi concluido!")
