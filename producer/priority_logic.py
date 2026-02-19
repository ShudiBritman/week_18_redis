def classifies_events(event):
    weapons_count= event['weapons_count']
    distance_from_fence_m = event['distance_from_fence_m']
    people_count = event['people_count']
    vehicle_type = event['vehicle_type']
    if weapons_count > 0:
        return True
    elif distance_from_fence_m <= 50:
        return True
    elif people_count >= 8:
        return True
    elif vehicle_type == "truck":
        return True