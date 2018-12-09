from pymongo import MongoClient
from matplotlib import pyplot

uri ="mongodb://admin:admin@ds021182.mlab.com:21182/c4e"
client = MongoClient(uri)

db = client.get_database()
customer_collection = db["customers"]

ref1 = 0
ref2 = 0
ref3 = 0

for dicts in customer_collection.find():
    if dicts["ref"] == "events":
        ref1 += 1
    elif dicts["ref"] == "ads" :
        ref2 += 1
    elif dicts["ref"] == "wom":
        ref3 += 1

print("the number of customers are acquired from events: ", ref1)
print("the number of customers are acquired from advertisements: ", ref2)
print("the number of customers are acquired from word of mouth: ", ref3)

details = [ref1, ref2, ref3]
names = ["events", "advertisements", "word of mouth"]

pyplot.pie(details, labels = names, autopct = "%.1f%%")
pyplot.axis("equal")
pyplot.show()


client.close()