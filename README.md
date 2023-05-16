# Schulklos kaputt

## Purpose
The purpose of this webserver is to display a live counter of the number of broken
toilets in the HTL Mödling.

## Start server
To start the server, create a virtual environment by running following command in the command line.
```
python -m venv venv
```
Then, activate it by executing the activate.bat file located at venv/scripts/activate.
To install the dependencies, run:
```
pip install -r requirements.txt
```
Finally, when the venv is activated, run
```
flask run
```
in the command prompt.
The Server will start on Port 5000.
