import redis
import os


REDIS_HOST = os.getenv("REDIS_HOST")
REDIS_PORT = int(os.getenv("REDIS_PORT"))

def get_connection():
    r = redis.Redis(host=REDIS_HOST, port=REDIS_PORT)
    return r