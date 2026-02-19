from mongo_connection import MongoConnection


def get_collection():
    return MongoConnection().get_collection()


class Queri:
    @staticmethod
    def border_distribution():
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
        return {cursor, result}


    @staticmethod
    def top_5_area():
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
        return list(coll.aggregate(pipline))
        

    @staticmethod
    def distance_distribution():
        coll = get_collection()
    

    @staticmethod
    def dangerous_area():
        coll = get_collection()


    @staticmethod
    def close_and_urgent_alerts():
        coll = get_collection()

