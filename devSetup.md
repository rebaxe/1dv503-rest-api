# How to set up project for development environment

Run the following command to setup a virtual environment locally:

### macOS

`python3 -m venv .venv source .venv/bin/activate`

### Windows

`py -3 -m venv .venv .venv\scripts\activate`

Update the virtual environment:
`python -m pip install --upgrade pip`

Install the following dependencies:
`python -m pip install flask`
`python -m pip install flask-mysql`
