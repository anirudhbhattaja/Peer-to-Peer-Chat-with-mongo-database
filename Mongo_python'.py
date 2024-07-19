#mongodb://localhost:27017

import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["Cricket"]

mycol = mydb["test_collection"]
print(mydb.list_collection_names())



myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["Chat_Room"]
mycol = mydb["User_Data"]

mydict = { "name": "John", "address": "Highway 37" }

x = mycol.insert_one(mydict)

print(x) 