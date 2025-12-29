import pymongo;

client = pymongo.MongoClient("mongodb://localhost:27017/")

db = client["mwp"]

collection = db["emp"]

dictionary = {
    "name":"Krishna",
    "age":20
}
# print(collection.insert_one(dictionary));
data =collection.find_one() 
print(data["name"])
print(data["age"])

for key in data.values():
    print(key)