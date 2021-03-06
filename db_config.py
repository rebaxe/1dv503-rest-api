from flaskext.mysql import MySQL
from pymysql import MySQLError
from create_tables import create_table_others, create_table_students, create_table_staff,create_table_houses
from populate_db import populate_db_houses, populate_db_students_staff_others 
from create_views import create_views
import os

def create_db(cursor, DB_NAME):
  try:
    # Create database.
    cursor.execute("CREATE DATABASE {} DEFAULT CHARACTER SET 'utf8'".format(DB_NAME))
  except MySQLError as err:
    print("Faild to create database {}".format(err))
    exit(1)

def connect_db(app):
  # Configure MySQL 
  app.config['MYSQL_DATABASE_USER'] = os.getenv('MYSQL_USER')
  app.config['MYSQL_DATABASE_PASSWORD'] = os.getenv('MYSQL_PASSWORD')
  app.config['MYSQL_DATABASE_PORT'] = int(os.getenv('MYSQL_PORT'))
  app.config['MYSQL_DATABASE_HOST'] = os.getenv('MYSQL_HOST')
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
      create_table_staff(cursor)
      create_table_others(cursor)
      create_table_houses(cursor)

      populate_db_students_staff_others(cursor, cnx)
      populate_db_houses(cursor, cnx)

      create_views(cursor)

      return cnx
  else: 
    print("Database {} exists".format('harrypotter'))
    return cnx