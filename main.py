from tkinter import *

from pytube import YouTube




escolha = int(input('Escolha o metodo de download: '))

if escolha == 1:
    url = input('Digite o link do vídeo: ')
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

    print('Download completo!!!')

    janela = Tk()
    janela.title('interface de python')
    janela.geometry('300x300')
    # janela.config(bg='purple')
    janela.resizable(width=False, height=False)

    texto_orientacao = Label(janela, text='Escolha o metodo')
    texto_orientacao.grid(column=0, row=0)

    botao = Button(janela, text='Clique aqui para executar', command='')

    janela.mainloop()