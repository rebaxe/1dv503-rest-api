# Hogwarts Wiki

A REST API serving information about Hogwarts related characters and the four houses.

## How to set up project for development environment

Run the following command to setup a virtual environment locally:

### macOS

`python3 -m venv .venv`<br>
`source .venv/bin/activate`

### Windows

`py -3 -m venv .venv .venv\scripts\activate`

### Installation

Update the virtual environment:
`python -m pip install --upgrade pip`

Install dependencies:
`python -m pip install -r requirements.txt`

### Environment variables

1. Create a file named `.env` in the root folder.
2. Add following variables in the file:

   `MYSQL_USER=<user>` <br>
   `MYSQL_PASSWORD=<password>` <br>
   `MYSQL_PORT=<port>`<br>
   `MYSQL_HOST=<host>`<br>

   Example: <br>
   `MYSQL_USER=root` <br>
   `MYSQL_PASSWORD=root` <br>
   `MYSQL_PORT=8889`<br>
   `MYSQL_HOST=localhost`<br>

You can adjust the environment settings according to your preferences.

## Run

`python -m flask run`

In the console you will find the address where your application is now running. By default, Flask will host the application at http://127.0.0.1:5000.

## Routes

`/houses/<housename>`
Returns information about a house. Valid houses are: gryffindor, hufflepuff, ravenclaw, slytherin.

`/houses/<housename>/characters`
Returns all characters that belong to a given house (gryffindor, hufflepuff, ravenclaw, slytherin).

`/houses/heads`
Returns information about the houses and their heads.

`/houses/total-students`
Returns the total number of students that belongs to each house.

`/characters/<name>`
Returns all characters that matches the name.

`/characters/students`
Returns all student characters.

`/characters/staff`
Returns all staff characters.

`/characters/others`
Returns all other characters.
