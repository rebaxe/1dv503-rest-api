import json

def house(cursor, house_name):

  query ="SELECT * FROM houses WHERE name = '{}'".format(house_name)

  cursor.execute(query)

  # Get row headers
  row_headers=[x[0] for x in cursor.description]
  result = cursor.fetchall()
  json_data=[]
  for r in result:
      json_data.append(dict(zip(row_headers,r)))
  return json.dumps(json_data)

def house_characters(cursor, house_name):

  query ="SELECT * FROM all_characters WHERE house = '{}'".format(house_name)

  cursor.execute(query)

  # Get row headers
  row_headers=[x[0] for x in cursor.description]
  result = cursor.fetchall()
  json_data=[]
  for r in result:
      json_data.append(dict(zip(row_headers,r)))
  return json.dumps(json_data)

def house_heads(cursor):
  query ="SELECT staff.name AS head_name, staff.species, staff.gender, staff.patronus, staff.wizard, staff.image, houses.name as house_name, houses.animal, houses.ghost, houses.founder, houses.element, houses.first_color, houses.second_color From staff JOIN houses ON (staff.name = houses.head)"

  cursor.execute(query)

  # Get row headers
  row_headers=[x[0] for x in cursor.description]

  result = cursor.fetchall()
  json_data=[]
  for r in result:
      json_data.append(dict(zip(row_headers,r)))
  return json.dumps(json_data)

def house_total_students(cursor):
  query ="SELECT houses.name, COUNT(students.name) AS total_students FROM houses	JOIN students ON (houses.name = students.house) GROUP BY houses.name ASC"

  cursor.execute(query)

  # Get row headers
  row_headers=[x[0] for x in cursor.description]

  result = cursor.fetchall()
  json_data=[]
  for r in result:
      json_data.append(dict(zip(row_headers,r)))
  return json.dumps(json_data)

def character_by_name(cursor, name):
  query="SELECT * FROM all_characters WHERE name LIKE '%{}%'".format(name)

  cursor.execute(query)

  # Get row headers
  row_headers=[x[0] for x in cursor.description]
  result = cursor.fetchall()
  json_data=[]
  for r in result:
      json_data.append(dict(zip(row_headers,r)))
  return json.dumps(json_data)

def all_from_table(cursor, table):
  query="SELECT * FROM {}".format(table)

  cursor.execute(query)

  # Get row headers
  row_headers=[x[0] for x in cursor.description]
  result = cursor.fetchall()

  json_data=[]
  for r in result:
      json_data.append(dict(zip(row_headers,r)))
  return json.dumps(json_data)
