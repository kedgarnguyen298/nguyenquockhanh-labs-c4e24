from pymongo import MongoClient

#1. Connect to database server
uri = "mongodb://admin:kedgarlovejun1312@ds127634.mlab.com:27634/c4e24-lab1-nqk"
client = MongoClient(uri)

#2. Select database
db = client.get_database()

#3. Select collection
post_collection = db["posts"]

# #4. Create document
# new_document = {
#     "title": "Hom nay troi ram",
#     "post": "Minh van o nha code tiep"
# }

# #5. Add document into collection
# post_collection.insert_one(new_document)

# print all data_base on post_collection
for post in post_collection.find():
    print(post)

#6. Close connection
client.close()