from pymongo import MongoClient

connection = MongoClient('localhost', 27017)

db = connection.students

grades = db.grades

for grd in grades.aggregate([{"$match": {"type": "homework"}},
                             {"$group": {"_id": "$student_id", "min": {"$min": '$score'}}},
                             {"$sort": {"score": -1}}
                             ]):
    print grades.delete_one({"student_id": grd["_id"], "score": grd["min"]})


