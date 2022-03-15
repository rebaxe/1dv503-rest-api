import json

def populate_db_students_staff_others(cursor, cnx):
  # Read JSON
  data = open('./data.json').read()
  json_data = json.loads(data)

  # Parse JSON and insert in DB
  for i, item in enumerate(json_data):
    name = item.get("name")
    house = item.get("house")
    species = item.get("species")
    gender = item.get("gender")
    patronus = item.get("patronus")
    wizard = item.get("wizard")
    image = item.get("image")

    isStudent = item.get("hogwartsStudent")
    isStaff = item.get("hogwartsStaff")

    if isStudent == True:
      if house != None:
        # Inserting into students
        query = "INSERT INTO students (name, house, species, gender, patronus, wizard, image) VALUES (%s,%s,%s,%s,%s,%s,%s)"
        cursor.execute(query, (name, house, species, gender, patronus, wizard, image))
    elif isStaff == True:
      # Inserting into staff
      query = "INSERT INTO staff (name, house, species, gender, patronus, wizard, image) VALUES (%s,%s,%s,%s,%s,%s,%s)"
      cursor.execute(query, (name, house, species, gender, patronus, wizard, image))
    else: 
      query = "INSERT INTO others (name, house, species, gender, patronus, wizard, image) VALUES (%s,%s,%s,%s,%s,%s,%s)"
      cursor.execute(query, (name, house, species, gender, patronus, wizard, image))
  cnx.commit()

def populate_db_houses(cursor, cnx):
  # Read JSON
  data = open('./houses.json').read()
  json_data = json.loads(data)

  # Parse JSON and insert in DB
  for i, item in enumerate(json_data):
    name = item.get("name")
    animal = item.get("animal")
    head = item.get("head")
    ghost = item.get("ghost")
    founder = item.get("founder")
    element = item.get("element")    
    first_color = item.get("first_color")
    second_color = item.get("second_color")

    # Inserting into houses
    query = "INSERT INTO houses (name, animal, head, ghost, founder, element, first_color, second_color) VALUES (%s,%s,%s,%s,%s,%s,%s,%s)"
    cursor.execute(query, (name, animal, head, ghost, founder, element, first_color, second_color))
 
  cnx.commit()
