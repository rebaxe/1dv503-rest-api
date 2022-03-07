from flask import Flask
from flaskext.mysql import MySQL
from db_config import connect_db
from queries import *

app = Flask(__name__)

# Connect to DB
cnx = connect_db(app)
cursor = cnx.cursor()


@app.route("/", methods=['GET'])
def home():
    return {"message": "Hello World!"}

@app.route("/houses/<housename>/characters", methods=['GET'])
def get_house_characters(housename):
    return house_characters(cursor, housename)

@app.route("/houses/heads", methods=['GET'])
def get_house_heads():
    return house_heads(cursor)

@app.route("/houses/total-students", methods=['GET'])
def get_house_total_students():
    return house_total_students(cursor)

if __name__ == '__main__':
  app.run()

# cursor.close()
# cnx.close()