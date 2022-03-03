from flask import Flask
from flaskext.mysql import MySQL

from db_config import connect_db

app = Flask(__name__)

# Connect to DB
cnx = connect_db(app)
cursor = cnx.cursor()

@app.route("/", methods=['GET'])
def home():
    return {"message": "Hello World!"}

if __name__ == '__main__':
  app.run()