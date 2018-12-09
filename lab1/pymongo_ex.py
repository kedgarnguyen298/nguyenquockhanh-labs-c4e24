from pymongo import MongoClient

#1. Connect to database server
uri = "mongodb://admin:kedgarlovejun1312@ds127634.mlab.com:27634/c4e24-lab1-nqk"
client = MongoClient(uri)

#2. Select database
db = client.get_database()

#3. Select collection
post_collection = db["accounts"]

#4. Create documents:
accounts = [
    {
        "username": "admin1",
        "password": "123456",
        "email": "admin1@abc.com",
        "phonenumber": "012345678",
        "yob": "1999"
    },

    {
        "username": "admin2",
        "password": "123456",
        "email": "admin2@abc.com",
        "phonenumber": "012345679",
        "yob": "1998"
    },

    {
        "username": "admin3",
        "password": "123456",
        "email": "admin@123.com",
        "phonenumber": "012345670",
        "yob": "1996"
    }
]
#5. Add document into collection:
for account in accounts:
    post_collection.insert_one(account)

#5. Print all accounts:
for account in post_collection.find():
    print(account)

# close client:
client.close()