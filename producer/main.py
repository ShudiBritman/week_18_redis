from redis_connection import get_connection
from priority_logic import Classifies
import json



def load_json():
    with open("./border_alert.json", "r") as f:
        data = json.load(f)
    return data


def send_to_redis(queue, event, count):
    r = get_connection()
    metadata = {
        'id':count,
        'from':'urgency_managment'
        }
    r.lpush(queue, json.dumps(metadata))
    r.hmset(f'message:{metadata["id"]}', {
        'state': json.dumps(event),
        'ttl':ttl
    })
    r.expire(f'message:{metadata['id']}', 300)


def main():
    events = load_json()
    updates_events = Classifies.classifies_urgency(events)
    for event in updates_events:
        urgent_count = 1
        normal_count = 1
        if event['priority'] == 'URGENT':
            send_to_redis("queue_urgent", event, urgent_count)
            urgent_count += 1
        else:
            send_to_redis("queue_normal", event, normal_count)
            normal_count += 1
        


if __name__ == "__main__":
    main()