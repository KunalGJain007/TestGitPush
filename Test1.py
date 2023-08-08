import pymongo
client = pymongo.MongoClient("mongodb+srv://kunalgjainds:AsGfmvzg01BCEk8R@cluster0.7azhjni.mongodb.net/?retryWrites=true&w=majority")
db = client.test
print(db)

d = {
    "name" : "kunal",
    "mail" : "kunal@gmail.com",
    "surname" : "jain",
     }

k = [9,18,27,36,45]
db1 = client['mongotest']
coll = db1['test']
coll.insert_one(d)