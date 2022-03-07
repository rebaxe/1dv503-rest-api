import json

def populate_db(cursor, cnx):
  # Read JSON
  data = open('./data.json').read()
  json_data = json.loads(data)

  # Parse JSON and insert in DB
  for i, item in enumerate(json_data):
    name = item.get("name")
    house = item.get("house")
    isStudent = item.get("hogwartsStudent")
    isStaff = item.get("hogwartsStaff")

    if isStudent == True:
      # Inserting into students
      query = "INSERT INTO students (name, house) VALUES (%s,	%s)"
      cursor.execute(query, (name,	house))

    if isStaff == True:
      # Inserting into staff
      query = "INSERT INTO staff (name, house) VALUES (%s,	%s)"
      cursor.execute(query, (name,	house))
  cnx.commit()
