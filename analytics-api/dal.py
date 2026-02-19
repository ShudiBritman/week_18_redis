from mongo_connection import MongoConnection


def get_collection():
    return MongoConnection().get_collection()


