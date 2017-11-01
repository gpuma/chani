import pymongo

connection = pymongo.MongoClient("mongodb://localhost")

def insert_item(item):
    db = connection.chani
    #todo: might need to refactor the name of this collection
    items=db.items

    new_item = {
        "item": item.name,
        "unit": item.unit,
        "quantity": item.quantity,
        "price": item.price,
        "currency": item.currency,
        "place": item.place,
        "date": item.date
    }

    try:
        items.insert_one(new_item)
        return 0
    except Exception as e:
        #todo: remove raise
        raise(e)
        return -1
