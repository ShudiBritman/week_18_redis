

class Classifies:

    @staticmethod
    def classifies_event(event):
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
        return None
        
    @staticmethod
    def check_combine_condition(event):
        distance_from_fence_m = event['distance_from_fence_m']
        people_count = event['people_count']
        vehicle_type = event['vehicle_type']
        if people_count >= 4 and distance_from_fence_m <= 150:
            return True
        elif people_count >= 3 and vehicle_type == "jeep":
            return True
        return None
    
    @staticmethod
    def classifies_urgency(events):
        events_update = []
        for event in events:
            is_urgency = Classifies.classifies_event(event)
            if is_urgency:
                event['priority'] = 'URGENT'
            else:
                is_urgency = Classifies.check_combine_condition(event)
                if is_urgency:
                    event['priority'] = 'URGENT'
                else:
                    event['priority'] = 'NORMAL'
            events_update.append(event)
        return events_update

    