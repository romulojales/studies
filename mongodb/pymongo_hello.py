import pymongo
from pymongo import MongoClient

connection = MongoClient('localhost', 27017)

db = connection.names

names = db.names

item = names.find_one()
print item["name"]
