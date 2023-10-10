# AirBnB_clone 
# Project Description

Welcome to the AirBnB clone project! This project involves building a command interpreter to manage AirBnB objects and serves as the first step towards creating a full web application. The command interpreter allows you to create, retrieve, update, and delete objects related to AirBnB properties.

# COMMAND INTERPRETER:

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

# Installing:

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


# How You Can Use It :

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

# Format of command Input:

In order to give commands to the console, these will need to be piped through an echo in case of Non-interactive mode.

In Interactive Mode the commands will need to be written with a keyboard when the prompt appears and will be recognized when an enter key is pressed (new line). As soon as this happens, the console will attempt to execute the command through several means or will show an error message if the command didn't run successfully. In this mode, the console can be exited using the CTRL + D combination, CTRL + C, or the command quit or EOF.


# Arguments:

Most commands have several options or arguments that can be used when executing the program. In order for the Shell to recognize those parameters, the user must separate everything with spaces.

Example:

user@ubuntu:~/AirBnB$ ./console.py

(hbnb) create BaseModel

49faff9a-6318-451f-87b6-910505c55907

user@ubuntu:~/AirBnB$ ./console.py

 

or

user@ubuntu:~/AirBnB$ ./console.py $ echo "create BaseModel" | ./console.py

(hbnb)

e37ebcd3-f8e1-4c1f-8095-7a019070b1fa

(hbnb)

user@ubuntu:~/AirBnB$ ./console.py

# Available commands and what they do:

The recognizable commands by the interpreter are the following:


| command | Description|
| --- | --- |
| quit or EOF | Exits the program 
| usage  | By itself |
| help   | Provides a text describing how to use a command |
| usage. | By itself --or-- help <command> |
| create | Creates a new instance of a valid class,saves it (to JSON file) and prints the id. Valid classes are,BaseModel,User,State,City,Amenity,Place and Review) |
| usage  | create <class name> |
| show   | Prints the string representation of an instance based on the class name and id |
| Usage | Shows  <class name>  <id>  --or--  <class name> .show(<id>) |
| destroy | Deletes an instance based on the class name and id then saves changes into a JSON file.) |
| Usage | destroy <class name> <id> --or-- destroy() |
| all  | Prints all string representation of all instances based or not on the class name |
|usage  | By itself or all <class name> --or-- <class name>.all() |
|update  | updates an instance based on the class name and id by adding or updating attributes then saves changes into a JSON file) |
|usage  |  update <class name> <id>  <attribute> "<attribute value>" ---or--- <class name>.update(<id>, <attribute name>,<attribute value>) --or-- <class name>.update(<id>,<dictionary representation>) |
| count  | Retrieve the number of instances of a class |
| usage  |  |<class name>.count() |

