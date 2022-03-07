import json

def populate_db(cursor, cnx):
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
      # Inserting into students
      query = "INSERT INTO students (name, house, species, gender,patronus, wizard, image) VALUES (%s,	%s,%s,%s,%s,%s,%s)"
      cursor.execute(query, (name,	house, 	 species, gender, patronus, wizard, image))

    if isStaff == True:
      # Inserting into staff
      query = "INSERT INTO staff (name, house, species, gender,patronus, wizard, image) VALUES (%s,	%s,%s,%s,%s,%s,%s)"
      cursor.execute(query, (name,	house, 	 species, gender, patronus, wizard, image))
  cnx.commit()
