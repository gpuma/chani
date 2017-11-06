import pymongo
from PriceItem import PriceItem

connection = pymongo.MongoClient("mongodb://localhost")
db = connection.chani
#todo: might need to refactor the name of this collection
items=db.items

def get_items(query={}):
    """returns all documents in 'items' collection
    as a list of PriceItem objects in ascending order of price"""
    results = items.find({"$text":{"$search": query}}).sort("price",1) if type(query)==str else items.find({})
    return [PriceItem.from_document(doc)  for doc in results]

def insert_item(item):
    try:
        items.insert_one(item.to_document())
        return 0
    except Exception as e:
        #todo: remove raise
        raise(e)
        return -1
