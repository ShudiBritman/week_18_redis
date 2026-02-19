import redis
import json


r = redis.Redis(host='localhost', port=6379)

metadata = {
    'id':'4',
    'from':'producer123',
    'signal_code': 'abcde'
}

r.lpush('my_first_list_queue', json.dumps(metadata))

ttl = 420
r.hmset(f'message:{metadata["id"]}', {
    'state': '...',
    'ttl':ttl
})


r.expire(f'message:{metadata['id']}', ttl)
# print("Message metadata pushed to the queue, full message details stored in Redis, and expiration set.")
