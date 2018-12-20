from youtube_dl import YoutubeDL

#1. Download a video from YT:
dl = YoutubeDL()
dl.download(["https://www.youtube.com/watch?v=WHK5p7JL7g4"])

#2. Download multiple YT videos:
dl.download(['https://www.youtube.com/watch?v=wNVIn-QS4DE', 'https://www.youtube.com/watch?v=JZjRrg2rpic'])

#3. Download audio:
options = {"format": "bestaudio/audio"}

dl_audio = YoutubeDL(options)
dl_audio.download(["https://www.youtube.com/watch?v=c3jHlYsnEe0"])

#4. Search and download first video:
options_2 = {
    "default_search": "ytsearch",
    "max_downloads": 1
}

dl_options_2 = YoutubeDL(options_2)
dl_options_2.download(["tam ka PKL"])

#5. Search and download first audio:
options_3 = {
    "default_search": "ytsearch",
    "max_downloads": 1,
    "format": "bestvideo/audio"
}

dl_options_3 = YoutubeDL(options_3)
dl_options_3.download(["Demons"])