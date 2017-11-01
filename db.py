import pymongo

connection = pymongo.MongoClient("mongodb://localhost")

#def get_items():

def insert_item(item):
    db = connection.chani
    #todo: might need to refactor the name of this collection
    items=db.items

    try:
        items.insert_one(item.to_document())
        return 0
    except Exception as e:
        #todo: remove raise
        raise(e)
        return -1
