from app import app

@app.route('/')
@app.route('/index')
def index():
    user  = {'username':'RAUNAQ'}
    return '''
    <html>
    <head>
      <title>HOME PAGE - MICROBLOGger</title>
        </head>
        <body bgcolor = 'blue'>
        <h1>Hello, ''' + user['username'] + '''</h1>
         </body>
         </html>'''
    
