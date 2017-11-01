from bottle import route, run, static_file, template, get, post, request

import db
#todo: maybe put this inside the function uses it
import re
import datetime
from PriceItem import PriceItem


view_folder='views'

@route('/')
def home():
    #return "Hola mundo!"
    #return static_file('home.html',root=view_folder)
    info = {'variable':'prueba'}
    return template('index.tpl', info)

# when we enter a new item (insert)
@post('/item/new')
def new_item():
    newItemExp=request.forms.get('newItemExp')
    item = process_item_exp(newItemExp)
    if db.insert_item(item) != 0:
        return "error insertando!"
    return "éxito papá!";

def process_item_exp(item_exp):
    """Extrae los componentes de una cadena 'item_exp'
    con el siguiente formato y retorna un objeto PriceItem:
    1kg de palta a 12 soles, centro
    250g de chia a 3 soles, ceylan"""

    pattern='(\d+)(\w+)\s+de\s+(\w+)\s+a\s+(\d+)\s+(\w+)\s*,\s*(\w+)'
    m=re.search(pattern, item_exp)
    #usamos datetime.datetime en vez de datetime.date porque pymongo
    #soloi soporta la codificación directa del primer tipo
    item=PriceItem(m.group(3),m.group(2),m.group(1),m.group(4),m.group(5),m.group(6),datetime.datetime.today())
    return item

run(host='localhost',port=80, debug=True, reloader=True)
#run(host='localhost',port=80, debug=True)
