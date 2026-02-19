import redis
import os


REDIS_HOST = os.getenv("REDIS_HOST")
REDIS_PORT = int(os.getenv("REDIS_PORT"))

def get_connection():
    r = redis.Redis(host=REDIS_HOST, port=REDIS_PORT)
    return r


def check_if_exist(key):
    r = get_connection()
    if r.exists(key):
        return r.get(key)
    return None


def save_in_redis(key, value):
    r =get_connection()
    r.set(key, value, ex=300)