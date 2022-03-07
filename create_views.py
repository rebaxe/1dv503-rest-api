from pymysql import MySQLError

def create_views(cursor):
  try:
    query = "CREATE VIEW all_characters AS SELECT name, house FROM students UNION SELECT name, house FROM staff"
    cursor.execute(query)

  except MySQLError as e:
    if e.args[0] == 1050:
      print("View all_characters exists")
    print("Failed to create view all_characters", e)

