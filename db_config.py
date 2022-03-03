from flaskext.mysql import MySQL
from pymysql import MySQLError
from create_tables import create_table_students
from populate_db import populate_db 

def create_db(cursor, DB_NAME):
  try:
    # Create database.
    cursor.execute("CREATE DATABASE {} DEFAULT CHARACTER SET 'utf8'".format(DB_NAME))
  except MySQLError as err:
    print("Faild to create database {}".format(err))
    exit(1)

def connect_db(app):
  # Configure MySQL 
  app.config['MYSQL_DATABASE_USER'] = 'root'
  app.config['MYSQL_DATABASE_PASSWORD'] = 'root'
  app.config['MYSQL_DATABASE_HOST'] = 'localhost'
  app.config['MYSQL_DATABASE_PORT'] = 8889

  try:
    mysql = MySQL(app)
    cnx = mysql.connect()
    cursor = cnx.cursor() 
    cursor.execute("USE {}".format('harrypotter'))
  except MySQLError as e:
    if e.args[0] == 1049:
      create_db(cursor, 'harrypotter')
      cnx.select_db('harrypotter')
      create_table_students(cursor)
      populate_db(cursor, cnx)
      return cnx
  else: 
    print("Database {} exists".format('harrypotter'))
    return cnx