from urllib.request import urlopen
from bs4 import BeautifulSoup
import pyexcel
from collections import OrderedDict

#1. Download trang
url =  "https://dantri.com.vn"
#1.1: Open a connection to server
conn = urlopen(url)
#1.2: Read data
raw_data = conn.read()
#1.3 Decode data
page_content = raw_data.decode("utf8")

# print(page_content)

# f = open("dantri.html", "wb")
# f.write(raw_data)
# f.close()



#2. Extra ROI
soup = BeautifulSoup(page_content, "html.parser")

ul = soup.find("ul", "ul1 ulnew") #id="ul1 ulnew"

#3. Extract data
li_list = ul.find_all("li")

# for li in li_list:
#     print(li.prettify())

news_list = []
for li in li_list:
    a= li.h4.a
    title = a.string
    link =url + a["href"]
    news = OrderedDict({
        "Title": title,
        "Link": link
    })
    news_list.append(news)

print(news_list)

#4. Save data to excel

pyexcel.save_as(records = news_list, dest_file_name = "dantri.xlsx")
