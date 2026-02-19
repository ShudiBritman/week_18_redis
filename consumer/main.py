from redis_connection import get_connection
import json




def load_from_redis(queue):
    r = get_connection()
    metadata = r.brpop(queue)
    metadata_info = json.loads(metadata[1].decode('utf-8'))
    full_message = r.hgetall(f"message:{metadata_info['id']}")
    return full_message