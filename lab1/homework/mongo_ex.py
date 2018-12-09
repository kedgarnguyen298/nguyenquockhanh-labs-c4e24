from pymongo import MongoClient

# Connect to our class’s Mongo Database:
uri ="mongodb://admin:admin@ds021182.mlab.com:21182/c4e"
client = MongoClient(uri)

#Add a post to this collection:
db = client.get_database()
post_collection = db["post"]

status = {
    "name": "Nguyễn Quốc Khánh",
    "about c4e24": "Vài dòng về lớp hai tư. Thầy Huy, anh Đức rất ư nhiệt tình. Slide cả các giáo trình. Chi tiết, dễ hiểu về nhà học ngon. Kiến thức em vẫn còn non. Mong thầy chỉ bảo sau còn kiếm cơm ! ",
    "say to next general": "Ba bốn triệu có là bao. Dăm ba cái thẻ cào game chứ gì. Học thấy hiệu quả tức thì. Nghỉ game đến với thầy Huy ngay nào :D "
}

post_collection.insert_one(status)


client.close()

