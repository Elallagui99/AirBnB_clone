#!/usr/bin/python3
""" the console """

import cmd
from datetime import datetime
import models
from models.base_model import BaseModel
from models.user import User
from models.amenity import Amenity
from models.city import City
from models.review import Review
from models.place import Place
from models.state import State
import shlex  # for splitting the line along spaces except in double quotes

classes = {"BaseModel": BaseModel, "User": User, "Amenity": Amenity,
           "City": City, "Review": Review, "Place": Place, "State": State}


class HBNBCommand(cmd.Cmd):
    """ Class for the console """
    prompt = '(hbnb) '

    def do_EOF(self, arg):
        """ Exit console """
        return True

    def emptyline(self):
        """ overwriting te emptyline """
        return False

    def do_quit(self, arg):
        """ quit cmd to exit program """
        return True

    def key_value_parser(self, args):
        """ create a dictionary from a list of strings """
        new_dict = {}
        for arg in args:
            if "=" in arg:
                kvp = arg.split('=', 1)
                key = kvp[0]
                value = kvp[1]
                if value[0] == value[1] == '"':
                    value = shlex.split(value)[0].replace('_', ' ')
                else:
                    try:
                        value = int(value)
                    except ValueError:
                        try:
                            value = float(value)
                        except ValueError:
                            continue
                new_dict[key] = value
        return new_dict

    def do_create(self, arg):
        """ creates a new instance of a class """
        args = shlex.split(arg)
        if len(args) == 0:
            print("** class name missing **")
            return False
        if args[0] in classes:
            cls = eval(args[0])
            instance = cls()
            instance.save()
            print(instance.id)
        else:
            print("** class doesn't exist **")
            return False

    def do_show(self, arg):
        """ Prints an instance as a string based on the class and id """
        args = shlex.split(arg)
        if len(args) == 0:
            print("** class name missing **")
            return False
        if args[0] in classes:
            if len(args) > 1:
                key = args[0] + "." + args[1]
                if key in models.storage.all():
                    print(models.storage.all()[key])
                else:
                    print("** no instance found **")
            else:
                print("** instance id missing **")
        else:
            print("** class doesn't exist **")

    def do_destroy(self, arg):
        """ delete an instance based on the class and id """
        args = shlex.split(arg)
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] in classes:
            if len(args) > 1:
                key = args[0] + "." + args[1]
                if key in models.storage.all():
                    models.storage.all().pop(key)
                    models.storage.save()
                else:
                    print("** no instance found **")
            else:
                print("** instance id missing **")
        else:
            print("** class doesn't exist **")

    def do_all(self, arg):
        """ prints string representaton of instance """
        args = shlex.split(arg)
        obj_list = []
        if len(args) == 0:
            obj_dict = models.storage.all()
        elif args[0] in classes:
            obj_dict = models.storage.all(classes[args[0]])
        else:
            print("** class doesn't exist **")
            return False
        for key in obj_dict:
            obj_list.append(str(obj_dict[key]))
        print("[", end="")
        print(",".join(obj_list), end="")
        print("]")

    def do_update(self, arg):
        """Update an instance based on the class name, id, attribute & value"""
        args = shlex.split(arg)
        integers = ["number_rooms", "number_bathrooms", "max_guest",
                    "price_by_night"]
        floats = ["latitude", "longitude"]
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] in classes:
            if len(args) > 1:
                k = args[0] + "." + args[1]
                if k in models.storage.all():
                    if len(args) > 2:
                        if len(args) > 3:
                            if args[0] == "Place":
                                if args[2] in integers:
                                    try:
                                        args[3] = int(args[3])
                                    except ValueError:
                                        args[3] = 0
                                elif args[2] in floats:
                                    try:
                                        args[3] = float(args[3])
                                    except ValueError:
                                        args[3] = 0.0
                            setattr(models.storage.all()[k], args[2], args[3])
                            models.storage.all()[k].save()
                        else:
                            print("** value missing **")
                    else:
                        print("** attribute name missing **")
                else:
                    print("** no instance found **")
            else:
                print("** instance id missing **")
        else:
            print("** class doesn't exist **")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
