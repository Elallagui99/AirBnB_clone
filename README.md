# AirBnB Clone Project
* Group project
* Python
* OOP
![AirBnB Logo](https://www.pngitem.com/pimgs/m/132-1322125_transparent-background-airbnb-logo-hd-png-download.png)

## Description of the project
This is the first part of the AirBnB clone project where we worked on the backend of the project while the interface would be a console application in python.
the Data are stored in  json file with the help of json modue in python.

## Description of the command interpreter:
The interface of this application is just a command line interface, where users can interact ith the backend which was developed with python OOP programming.

Some of the available commands:
* show
* create
* update
* destroy
* count

In this application the following actions can be performed:
* Creating an object (ex: new user or new place)
* Retieving an object from a file(database)
* Doing opereations on the objects(count, compute stats...)
* Update the attributes of an object
* Destroy an object


### How to start it
Follow this instruction to start using the application:

#### Installing
you need to clone the repository from Github. this will contain the simple shell program and all of its dependesncies.
```
https://github.com/ScottShadow/AirBnB_clone.git
```
after cloning you will have a folder caller AirBnB_clone. In here will be severa files.
> /console.py : The main executable of the project, the command interpreter.
>
> models/engine/file_storage.py: Class that serializes instances to a JSON file and deserializes JSON file to instances
> 
> models/__ init __.py:  A unique `FileStorage` instance for the application
> 
> models/base_model.py: Class that defines all common attributes/methods for other classes.
> 
> models/user.py: User class that inherits from BaseModel
> 
>models/state.py: State class that inherits from BaseModel
>
>models/city.py: City class that inherits from BaseModel
>
>models/amenity.py: Amenity class that inherits from BaseModel
>
>models/place.py: Place class that inherits from BaseModel
>
>models/review.py: Review class that inherits from BaseModel
#### How to use it
it can work in two diffrent modes:
**Interactive** and **Non-interactive** mode:

In Interactive mode, the console will display a prompt (hbnb) indicating that the user can write the command to be executed, after that the prompt will  appear again and wait for a new command as long as the user does not exit the program(CTRL+D/C).
```
$ ./console.py
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  help  quit

(hbnb) 
(hbnb) 
(hbnb) quit
$
```
In Non-interactive mode , the shell will need to be run wit a command input piped into its execution so that the command is run as soon as the shell starts,. In this mode no prompt will appear, and further more input will be expected from the user.
```
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
```
#### Available commands and its job
NB: command nedd to be separated with a sppace in order to be recognized by the shell.

|Command| Description |
|--|--|
| **quit or EOF** | Exits the program |
| **Usage** | By itself |
| **-----** | **-----** |
| **help** | Provides a text describing how to use a command.  |
| **Usage** | By itself --or-- **help <command\>** |
| **-----** | **-----** |
| **create** | Creates a new instance of a valid `Class`, saves it (to the JSON file) and prints the `id`.  Valid classes are: BaseModel, User, State, City, Amenity, Place, Review. |
| **Usage** | **create <class name\>**|
| **-----** | **-----** |
| **show** | Prints the string representation of an instance based on the class name and `id`  |
| **Usage** | **show <class name\> <id\>** --or-- **<class name\>.show(<id\>)**|
| **-----** | **-----** |
| **destroy** | Deletes an instance based on the class name and `id` (saves the change into a JSON file).  |
| **Usage** | **destroy <class name\> <id\>** --or-- **<class name>.destroy(<id>)** |
| **-----** | **-----** |
| **all** | Prints all string representation of all instances based or not on the class name.  |
| **Usage** | By itself or **all <class name\>** --or-- **<class name\>.all()** |
| **-----** | **-----** |
| **update** | Updates an instance based on the class name and `id` by adding or updating attribute (saves the changes into a JSON file).  |
| **Usage** | **update <class name\> <id\> <attribute name\> "<attribute value\>"** ---or--- **<class name\>.update(<id\>, <attribute name\>, <attribute value\>)** --or-- **<class name\>.update(<id\>, <dictionary representation\>)**|
| **-----** | **-----** |
| **count** | Retrieve the number of instances of a class.  |
| **Usage** | **<class name\>.count()** |
