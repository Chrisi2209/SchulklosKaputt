# SCHULKLOS KAPUTT

## PURPOSE
The purpose of this webserver is to display a live counter of the number of broken toilets in the HTL Mödling. 

The live count is determined by a community of admins. The admin accounts need to directly be injected into the database.

# START SERVER
Note that you will need to have python 3 installed on your system to start the server directly on your machine. Otherwise, you can fall back to deploying it on docker but you will still need to have docker desktop installed for this method. If you don't have python, nore Docker Desktop installed, please install one of the two to deploy the server it. If you have a package already containing the database (migrations directory and app/app.db exist) and the virtual environment, you don't have to recreate the environment and database, just activate the venv and run the flask app. 

## START LOCALLY
To start the server, create a virtual environment by running following command in the command line.

```
python -m venv venv
```

Then, activate it by executing the activate.bat file located at venv/scripts/activate.

```
venv/scripts/activate
```

To install the dependencies, run:

```
pip install -r requirements.txt
```

Next, we need to create the database

```
flask db init
flask db migrate -m "initial"
flask db upgrade
```

Will create the database. Finally we can run the application using

```
flask run
```

The Server will start on Port 5000.

## DEPLOY ON DOCKER
To deploy the Webserver inside of a Docker-Container, you will need to have Docker Desktop installed. Next, you can build the Container by executing following command in the command line at the directory of the dockerfile.
```
docker build -t schulklos-kaputt .
```
_schulklos-kaputt_ is only the name of your image. You can exchange it for any other name, but remember to use the same name for every command.

To run the container on the image, run the following command:
```
docker run -dp 5000:5000 schulklos-kaputt
```
The second 5000 is the port, the service will be visible on. So go on and change it to your preference. Now, the container is running and you can access the website on localhost and the port you declared.

# DATABASE

## CREATE AN ADMIN ACCOUNT
To create admin accounts, run following command in the command prompt at the project directory to get into a shell where you can manipulate the database. If you are running inside a docker container, just access the terminal of the container.

```
flask shell
```

To create an account, now run following commands:

```python
new_admin = User(username="YOUR_USERNAME")
new_admin.set_password("YOUR_PASSWORD")
db.session.add(new_admin)
db.session.commit()
```

The new User should now be in the database and you can log in using it.

## DELETE AN ADMIN ACCOUNT
To delete an admin account, start the flask shell.

```
flask shell
```

Then query the Users and remove it from the database.

```python
User.query.all()  # display all the admins currently in the system
db.session.delete(User.query.all()[n])  # replace n with the index of the user, you want to delete
db.session.commit()
```

The deletion should now be complete.