import redis
import os
import json


REDIS_HOST = os.getenv("REDIS_HOST")
REDIS_PORT = int(os.getenv("REDIS_PORT"))

def get_connection():
    r = redis.Redis(host=REDIS_HOST, port=REDIS_PORT)
    return r


def check_if_exist(key):
    r = get_connection()
    if r.exists(key):
        result = r.get(key)
        data = json.loads(result)
        return data
    return None


def save_in_redis(key, value):
    r = get_connection()
    json_value = json.dumps(value)
    json_key = json.dumps(key)
    r.set(json_key, json_value, ex=300)