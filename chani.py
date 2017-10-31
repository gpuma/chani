from bottle import route, run, static_file, template

view_folder='views'

@route('/')
def home():
    #return "Hola mundo!"
    #return static_file('home.html',root=view_folder)
    info = {'variable':'prueba'}
    return template('index.tpl', info)

#run(host='localhost',port=80, debug=True, reloader=True)
run(host='localhost',port=80, debug=True)
