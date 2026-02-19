from mongo_connection import MongoConnection
from redis_connection import check_if_exist, save_in_redis


def get_collection():
    return MongoConnection().get_collection()


class Queri:
    @staticmethod
    def border_distribution():
        is_exist = check_if_exist("border_distribution")
        if is_exist:
            return is_exist
        else:
            coll = get_collection()
            query = {'border': 'URGENT'}
            projection = {'border':1, '_id':0}
            cursor = list(coll.find(query, projection))
            pipline = [
                {
                    '$group':{
                        '_id':{
                                'priority': '$priority',
                                'count': {'count': 'count'}
                        }
                    }
                },
                {'$project':
                {'_id':0,
                'priority':'$_id.priority',
                'count':'_id.count'}
                },
                {'$sort':{'count':-1}}
            ]
            result = list(coll.aggregate(pipline))
            save_in_redis('border_distribution', result)
            return {cursor, result}


    @staticmethod
    def top_5_area():
        is_exist = check_if_exist("top_5_area")
        if is_exist:
            return is_exist
        else:
            coll = get_collection()
            pipline = [
                {
                    '$group':{
                        '_id':{
                                'priority': '$priority',
                                'count': {'count': 'count'}
                        }
                    }
                },
                {'$project':
                {'_id':0,
                'priority':'$_id.priority',
                'count':'_id.count'}
                },
                {'$sort':{'count':-1}},
                {'$limit': 5}
            ]
            result = list(coll.aggregate(pipline))
            save_in_redis('top_5_area', result)
            return result
        

    @staticmethod
    def distance_distribution():
        is_exist = check_if_exist("distance_distribution")
        if is_exist:
            return is_exist
        else:
            coll = get_collection()
            save_in_redis()

    @staticmethod
    def dangerous_area():
        is_exist = check_if_exist("dangerous_area")
        if is_exist:
            return is_exist
        else:
            coll = get_collection()
            save_in_redis()


    @staticmethod
    def close_and_urgent_alerts():
        is_exist = check_if_exist("close_and_urgent_alerts")
        if is_exist:
            return is_exist
        else:
            coll = get_collection()
            save_in_redis()

