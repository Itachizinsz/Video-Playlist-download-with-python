from pytube import YouTube

url = input('Digite o link do vídeo: ')

youTube = YouTube(url)

print('iniciando')
print("Titulo: "+ youTube.title)
video = youTube.streams.get_highest_resolution()
video.download('C:\\xampp\\htdocs\\python\\teste_4_pytube\\music')
print('Download concluido!!!')