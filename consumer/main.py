from redis_connection import get_connection
from datetime import datetime
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