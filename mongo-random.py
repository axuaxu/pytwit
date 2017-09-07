#http://api.mongodb.com/python/current/index.html
#https://www.mongodb.com/blog/post/how-to-perform-random-queries-on-mongodb
#http://www.bogotobogo.com/python/MongoDB_PyMongo/python_MongoDB_pyMongo_tutorial_connecting_accessing.php
from pymongo import MongoClient


client = MongoClient("mongodb://localhost:27017")
db = client.flist
coll = db.flist
 
print(coll.find_one())
print(db.version)
#db.coll.aggregate([{$sample: {size: 1}}])