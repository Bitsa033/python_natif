from pytube import YouTube

link=input('entrez le lien de la vidéo: ')
video=YouTube(link)
stream=video.streams.get_highest_resolution()
stream.download()
