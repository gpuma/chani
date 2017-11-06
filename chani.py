from bottle import route, run, static_file, template, get, post, request, redirect, response

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
    #we use request.params instead of request.forms.get so
    #parameters are automatically converted to unicode strings

    #todo: refactor the name of this variable
    newItemExp=request.params.newItemExp
    item = process_item_exp(newItemExp)
    #when our regex doesn't match we'll assume the user
    #wanted to search instead of entering a new item
    if item is None:
        redirect("/items/"+newItemExp)
    if db.insert_item(item) != 0:
        return "error insertando!"
    redirect("/items");

@get('/items')
def show_items():
    #todo: make it more readable?
    return template('items.tpl', {'items' : db.get_items(), 'title': 'Todos' })

@get('/items/<q>')
def search_items(q):
    #for some reasone naming 'q' 'query' throws an error
    #response.content_type="Content-Type: text/html; charset=UTF-8"
    #q=request.query.q
    resultado = db.get_items(q)
    return template('items.tpl', {'items' : db.get_items(q), 'title':'Búsqueda','q': q})

def process_item_exp(item_exp):
    """Extrae los componentes de una cadena 'item_exp'
    con el siguiente formato y retorna un objeto PriceItem:
    1kg de palta a 12 soles en centro
    250g de chia a 3 soles en ceylan"""

    pattern='(\d+\.*\d*)\s*(.+)\s+de\s+(.+)\s+a\s+(\d+\.*\d*)\s+(\w+)\s+en\s+(.+)'
    #re.UNICODE supports accented characters (eg. café)
    m=re.search(pattern, item_exp.strip(), re.UNICODE)
    if m is None:
        return None
    #usamos datetime.datetime en vez de datetime.date porque pymongo
    #soloi soporta la codificación directa del primer tipo
    item=PriceItem(m.group(3),m.group(2),m.group(1),m.group(4),m.group(5),m.group(6),datetime.datetime.today())
    return item

@get('/favicon.ico')
def get_favicon():
    return static_file('favicon.ico',view_folder)

run(host='localhost',port=80, debug=True, reloader=True)
#run(host='localhost',port=80, debug=True)
