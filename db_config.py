from app import app
from flaskext.mysql import MySQL
# mysql = MySQL()
#
# # MySQL configurations
# app.config['MYSQL_DATABASE_USER'] = 'root'
# app.config['MYSQL_DATABASE_PASSWORD'] = 'Ranjith1'
# app.config['MYSQL_DATABASE_DB'] = 'mydb'
# app.config['MYSQL_DATABASE_HOST'] = 'localhost'
# mysql.init_app(app)

import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="yourusername",
  password="yourpassword"
)