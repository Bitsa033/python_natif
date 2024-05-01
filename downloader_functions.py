from pytube import YouTube
def dowload_video(url):
    url=input('entrez le lien de la vidéo: ')
    video=YouTube(url)
    stream=video.streams.get_highest_resolution()
    stream.download()
