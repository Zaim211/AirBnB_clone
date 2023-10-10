# AirBnB_clone
Project Description

Welcome to the AirBnB clone project! This project involves building a command interpreter to manage AirBnB objects and serves as the first step towards creating a full web application. The command interpreter allows you to create, retrieve, update, and delete objects related to AirBnB properties.

COMMAND INTERPRETER:

The interface of the application is just like the Bash shell except that this has limited number of accepted commands that were solely defined for the purposes of the usage of the AirBnB website.
This command line interpreter serves as the frontend of the web app where users can  interact with the backend which was developed with Python OOP Programming.
In our case, We want to be able to manage the objects of our project:

•Show 

•Create

•Update

•Count

•Destroy

As part of the implementation of the command line interpreter coupled with backend and file storage system, the following actions can be performed:

•Retrieve an object from a file, database and etc...

•Do operations on an objects(count,computer stats and etc...)

•Update attributes of an object

•Create new objects (eg, A New User or a new Place)

•Destroy an object

Installing:

You will need to clone the repository of the project from Github. This will contain the simple shell program and all of its dependencies.

 

git clone https://github.com/bontlenkoale1/AirBnB_clone.git

After cloning the repository you will have a folder called AirBnB_clone. In here there will be several files that allow the program to work.

/console.py : The main executable of the project, the command interpreter.

models/engine/file_storage.py: Class that serializes instances to a JSON file and deserializes JSON file to instances

models/__ init __.py: A unique FileStorage instance for the application

models/base_model.py: Class that defines all common attributes/methods for other classes.

models/user.py: User class that inherits from BaseModel

models/state.py: State class that inherits from BaseModel

models/city.py: City class that inherits from BaseModel

models/amenity.py: Amenity class that inherits from BaseModel

models/place.py: Place class that inherits from BaseModel

models/review.py: Review class that inherits from BaseModel


How You Can Use It :

It can work in two different modes:

Interactive and Non-interactive.

In Interactive mode, the console will display a prompt (hbnb) indicating that the user can write and execute a command. After the command is run, the prompt will appear again and wait for a new command. This can go indefinitely as long as the user does not exit the program.


$ ./console.py

(hbnb) help

 

Documented commands (type help <topic>):

========================================

EOF  help  quit

 

(hbnb)

(hbnb)

(hbnb) quit

$


In Non-interactive mode, the shell will need to be run with a command input piped into its execution so that the command is run as soon as the Shell starts. In this mode no prompt will appear, and no further input will be expected from the user.


$ echo "help" | ./console.py

(hbnb)

 

Documented commands (type help <topic>):

========================================

EOF  help  quit

(hbnb)

$

$ cat test_help

help

$

$ cat test_help | ./console.py

(hbnb)

 

Documented commands (type help <topic>):

========================================

EOF  help  quit

(hbnb)

$

