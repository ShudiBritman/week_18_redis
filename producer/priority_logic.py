def classifies_events(event):
    if event['weapons_count'] > 0:
        return True
    elif event['distance_from_fence_m'] <= 50:
        return True
    elif event['people_count'] >= 8:
        return True
    elif event['vehicle_type'] == "truck":
        return True
    


    