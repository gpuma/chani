import pymongo
from PriceItem import PriceItem

connection = pymongo.MongoClient("mongodb://localhost")
db = connection.chani
#todo: might need to refactor the name of this collection
items=db.items

def get_items():
    """returns all documents in 'items' collection
    as a list pf PriceItem objects"""
    return [PriceItem.from_document(doc)  for doc in items.find({})]

def insert_item(item):
    try:
        items.insert_one(item.to_document())
        return 0
    except Exception as e:
        #todo: remove raise
        raise(e)
        return -1
