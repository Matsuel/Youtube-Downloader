import pytube

link= input("Lien de la vidéo à télécharger")
yt= pytube.YouTube(link)

downloader = yt.streams.get_highest_resolution()
print("En cours de téléchargement")

downloader.download(filename= "Video_Download.mp4")
print("Finish")