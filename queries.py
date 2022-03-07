import json

def house_characters(cursor, house_name):
  query ="SELECT name, house FROM students WHERE house = '{}' UNION SELECT name, house FROM staff WHERE house = 'Gryffindor'".format(house_name)

  cursor.execute(query)
  
  row_headers=[x[0] for x in cursor.description] #this will extract row headers
  result = cursor.fetchall()
  json_data=[]
  for r in result:
      json_data.append(dict(zip(row_headers,r)))
  return json.dumps(json_data)


