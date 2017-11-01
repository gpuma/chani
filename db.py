import pymongo
from PriceItem import PriceItem

connection = pymongo.MongoClient("mongodb://localhost")
db = connection.chani
#todo: might need to refactor the name of this collection
items=db.items

def get_items(query={}):
    """returns all documents in 'items' collection
    as a list pf PriceItem objects"""
    #if type==str:
    results = items.find({"$text":{"$search": query}}) if type(query)==str else items.find({})
    #results = items.find({"$text":{"$search": query}}) if query is not None else items.find(query)
    return [PriceItem.from_document(doc)  for doc in results]

def insert_item(item):
    try:
        items.insert_one(item.to_document())
        return 0
    except Exception as e:
        #todo: remove raise
        raise(e)
        return -1
