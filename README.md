# SCHULKLOS KAPUTT

## PURPOSE
The purpose of this webserver is to display a live counter of the number of broken
toilets in the HTL Mödling.

## START SERVER
Note that you will need to have python 3 installed on your system to start the server directly on your machine. Otherwise, you can fall back to deploying it on docker but you will still need to have docker desktop installed for this method. If you don't have python, nore Docker Desktop installed, please install one of the two to deploy the server it.
## START LOCALLY
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

## DEPLOY ON DOCKER
To deploy the Webserver inside of a Docker-Container, you will need to have Docker Desktop installed. Next, you can build the Container by executing following command in the command line at the directory of the dockerfile.
```
docker build . -t Schulklos-kaputt
```
_Schulklos-kaputt_ is only the name of your image. You can exchange it for any other name, but remember to use the same name for every command.

To run the container on the image, run the following command:
```
docker run -dp 5000:5000 Schulklos-kaputt
```
The second 5000 is the port, the service will be visible on. So go on and change it to your preference. Now, the container is running and you can access the website on localhost and the port you declared.
