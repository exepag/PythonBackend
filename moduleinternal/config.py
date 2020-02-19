from flask import Flask,jsonify,request
from flaskext.mysql import MySQL

mysql = MySQL()
app = Flask(__name__)
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = 'qwer'
app.config['MYSQL_DATABASE_DB'] = 'customer'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
mysql.init_app(app)
HOST_SERVER = "http://18.139.222.3"
PORT_SERVICE = "9805"
HOST_SERVER_SERVICE = HOST_SERVER+":"+str(PORT_SERVICE)
