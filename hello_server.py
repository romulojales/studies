import bottle
from pymongo import MongoClient


@bottle.route("/")
def index():

    connection = MongoClient('localhost', 27017)

    db = connection.names

    names = db.names

    item = names.find_one()
    return "<b>Hello %s</b>" % item["name"]

bottle.run(host="localhost", port=8002)
