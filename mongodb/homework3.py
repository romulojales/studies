from pymongo import MongoClient


connection = MongoClient('localhost', 27017)

db = connection.school

students = db.students
for std in students.find():
    scores = std["scores"]
    idx = 0
    min_value = -1
    for idex, scr in enumerate(scores):

        if scr["type"] == "homework":
            if min_value == -1:
                min_value = scr["score"]
            elif  scr["score"] < min_value:
                 idx = idex

    if idx != 0:
        scores.pop(idx)
    students.update_one({"_id": std["_id"]}, {"$set":{"scores": scores}})
