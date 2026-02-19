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
    

def check_combine_condition(event):
    distance_from_fence_m = event['distance_from_fence_m']
    people_count = event['people_count']
    vehicle_type = event['vehicle_type']
    if people_count >= 4 and distance_from_fence_m <= 150:
        return True
    elif people_count >= 3 and vehicle_type == "jeep":
        return True
    