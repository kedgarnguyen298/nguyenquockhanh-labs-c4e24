from urllib.request import urlopen
from bs4 import BeautifulSoup
import pyexcel
from collections import OrderedDict
from youtube_dl import YoutubeDL

#1. Download page
url = "https://www.apple.com/itunes/charts/songs"
#1.1. Open connection to server
conn = urlopen(url)
#1.2. Read data
raw_data = conn.read()
#1.3. Decode data
page_content = raw_data.decode("utf-8")

#2. Extra ROI
soup = BeautifulSoup(page_content, "html.parser")
div = soup.find("div", id = "main")
ul = div.section.div.ul

#3. Extra data
li_list = ul.find_all("li")

top_song_list = []
for li in li_list:
    song_name = li.h3.a.string
    singer_name = li.h4.a.string
    song_link = li.h3.a["href"]
    top_song = OrderedDict({
        "Singer": singer_name,
        "Song": song_name,
        "Link": song_link
    })
    top_song_list.append(top_song)
#4. Save to the excel
pyexcel.save_as(records = top_song_list, dest_file_name = "topsong.xlsx")

#5. Download those from youtube
options = {
    "default_search": "ytsearch",
    "format": "bestaudio/audio"
}

dl = YoutubeDL(options)

for top_song in top_song_list:
    dl.download([top_song["Song"] + top_song["Singer"]])
