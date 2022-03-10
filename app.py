from flask import Flask
from flask_cors import CORS
from flaskext.mysql import MySQL
from db_config import connect_db
from queries import *

app = Flask(__name__)
CORS(app)

# Connect to DB
cnx = connect_db(app)
cursor = cnx.cursor()


@app.route("/", methods=['GET'])
def home():
    return {"message": "Hello Hogwarts World!"}

@app.route("/houses/<housename>/characters", methods=['GET'])
def get_house_characters(housename):
    return house_characters(cursor, housename)

@app.route("/houses/heads", methods=['GET'])
def get_house_heads():
    return house_heads(cursor)

@app.route("/houses/total-students", methods=['GET'])
def get_house_total_students():
    return house_total_students(cursor)

@app.route("/characters/<name>", methods=['GET'])
def get_character_by_name(name):
    return character_by_name(cursor, name)

@app.route("/characters/students", methods=['GET'])
def get_students():
    return all_from_table(cursor, "students")

@app.route("/characters/staff", methods=['GET'])
def get_staff():
    return all_from_table(cursor, "staff")

@app.route("/characters/others", methods=['GET'])
def get_others():
    return all_from_table(cursor, "others")

if __name__ == '__main__':
  app.run()
