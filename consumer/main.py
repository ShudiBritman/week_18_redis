from redis_connection import get_connection
from datetime import datetime
from mongo_connection import MongoConnection
import json




def load_from_redis(queue):
    r = get_connection()
    metadata = r.brpop(queue)
    metadata_info = json.loads(metadata[1].decode('utf-8'))
    full_message = r.hgetall(f"message:{metadata_info['id']}")
    return full_message

def add_insertion_time(alert):
    alert['time_insertion'] = datetime.now()
    return alert

def send_to_mongo(alert):
    mongo = MongoConnection()
    coll = mongo.get_collection()
    coll.insert_one(alert)


def managment():
    while True:
        alert = load_from_redis('queue_urgent')
        update_alert = add_insertion_time(alert)
        send_to_mongo(update_alert)
        if not alert:
            alert = load_from_redis('queue_normal')
            update_alert = add_insertion_time(alert)
            send_to_mongo(update_alert)


def main():
    managment()


if __name__ == "__main__":
    main()