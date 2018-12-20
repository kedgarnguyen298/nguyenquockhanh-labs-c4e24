from urllib.request import urlopen
from bs4 import BeautifulSoup
import pyexcel
from collections import OrderedDict

#1. Download and decode data
url = "http://s.cafef.vn/bao-cao-tai-chinh/VNM/IncSta/2017/3/0/0/ket-qua-hoat-dong-kinh-doanh-cong-ty-co-phan-sua-viet-nam.chn"
conn = urlopen(url)
raw_data = conn.read()
page_content = raw_data.decode("utf-8")

#2. Download page to html
f = open("cafef.html", "wb")
f.write(raw_data)
f.close()

#3. Extra ROI
soup = BeautifulSoup(page_content, "html.parser")

div = soup.find("div", style = "overflow:hidden;width:100%;border-bottom:solid 1px #cecece;")

#4. Extra data
tr_list_1 = div.find_all("tr", "r_item")
tr_list_2 = div.find_all("tr", "r_item_a")
tr_list = tr_list_1 + tr_list_2

statist = []
for tr in tr_list:
    td_list = tr.find_all("td")
    article = td_list[0].string
    quarter_4_2016 = td_list[1].string
    quarter_1_2017 = td_list[2].string
    quarter_2_2017 = td_list[3].string
    quarter_3_2017 = td_list[4].string
    details = OrderedDict({
        "Article": article,
        "Quy 4 2016": quarter_4_2016,
        "Quy 1 2017": quarter_1_2017,
        "Quy 2 2017": quarter_2_2017,
        "Quy 3 2017": quarter_3_2017
    })
    statist.append(details)

#5. Save to Excel
pyexcel.save_as(records = statist, dest_file_name = "cafef.xlsx")

