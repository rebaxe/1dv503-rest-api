from flaskext.mysql import MySQL

def connect_db(app):

  # Configure MySQL 
  app.config['MYSQL_DATABASE_USER'] = 'root'
  app.config['MYSQL_DATABASE_PASSWORD'] = 'root'
  app.config['MYSQL_DATABASE_DB'] = 'harry-potter'
  app.config['MYSQL_DATABASE_HOST'] = 'localhost'

  mysql = MySQL(app)
  return mysql