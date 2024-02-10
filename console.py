#!/usr/bin/python3
""" the console """

import cmd
from datetime import datetime
import models
from models.base_model import BaseModel
import shlex  # for splitting the line along spaces except in double quotes

classes = {"BaseModel": BaseModel}


class HBNBCommand(cmd.Cmd):
    """ Class for the console """
    prompt = '(hbnb) '

    def do_EOF(self, arg):
        """ Exit console """
        return True

    def emptyline(self):
        """ overwriting te emptyline """
        return False

    def do_quit(self):
        """ quit cmd to exit program """
        return False

    def key_value_parser(self, args):
        """ create a dictionary from a list of strings """
        new_dict = {}
        for arg in args:
            if "=" in arg:
                kvp = arg.split('=', 1)
                key = kvp[0]
                value = kvp[1]
                if value[0] == value[1] == '"':
                    value = shelex.split(value)[0].replace('_', ' ')
                else:
                    try:
                        value = int(value)
                    except ValueError:
                        try:
                            value = float(value)
                        except ValueError:
                            continue
                new_ict[key] = value
        return new_dict

    def do_create(self, arg):
        """ creates a new instance of a class """
        args = arg.split()
        if len(args) == 0:
            print("** class name missing **")
            return False
        if args[0] in classes:
            new_dict = self._key_value_parser(args[1:])
            instance = classes[args[0]](**new_dict)
        else:
            print("** class doesn't exist **")
            return False
        print(intance.id)
        instance.save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
