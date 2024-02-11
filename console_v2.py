import cmd
import shlex
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
""" the console """


class HBNBCommand(cmd.Cmd):
    """ Class for the console """
    models = ["BaseModel", "User", "City",
              "Place", "Review", "State", "Amenity"]
    prompt = "(hbnb)"

    def do_create(self, arg):
        """Creates a new instance of a model and saves it to a Json file"""
        model = shlex.split(arg)

        if len(model) < 1:
            print("** class name missing **")
            return False

        if model[0] in self.models:
            cls = eval(model[0])
            new_instance = cls()
            new_instance.save()
            print(new_instance.id)
        else:
            print("** class doesn't exist **")

    def do_show(self, arg):
        """
        Prints the string representation of an instance based on
        the class name and id
        """
        args = shlex.split(arg)
        if len(args) == 0:
            print("** class name missing **")
            return
        elif len(args) <= 1:
            if (args[0] not in self.models):
                print("** class doesn't exist **")
                return
            print("** instance id missing **")
            return
        objs = storage.all()
        obj_key = f"{args[0]}.{args[1]}"
        if obj_key in objs:
            print(objs[obj_key])
        else:
            print("** no instance found **")

    def do_destroy(self, arg):
        """
        Deletes an instance based on the class
        name and id (save the change into the JSON file).
        """
        args = shlex.split(arg)
        if len(args) == 0:
            print("** class name missing **")
            return
        elif len(args) <= 1:
            if (args[0] not in self.models):
                print("** class doesn't exist **")
                return
            print("** instance id missing **")
            return
        objs = storage.all()
        obj_key = f"{args[0]}.{args[1]}"
        if obj_key in objs:
            del objs[obj_key]
        else:
            print("** no instance found **")

    def do_all(self, arg):
        """
        Prints all string representation of all instances
        based or not on the class name.
        """
        objs = storage.all()
        args = shlex.split(arg)
        if len(args) == 0:
            for key, val in objs.items():
                print(str(val))
        elif args[0] not in self.models:
            print("** class doesn't exist **")
        else:
            for key, val in objs.items():
                if key.split(".")[0] == args[0]:
                    print(str(val))

    def do_update(self, arg):
        """
        Updates an instance based on the class name and id
        by adding or updating attribute (save the change into the JSON file)
        """
        objs = storage.all()
        args = shlex.split(arg)
        if len(args) == 0:
            print("** class name missing **")
            return
        elif len(args) <= 1:
            if (args[0] not in self.models):
                print("** class doesn't exist **")
                return
            print("** instance id missing **")
            return
        objs = storage.all()
        obj_key = f"{args[0]}.{args[1]}"

        if len(args) < 3:
            if obj_key not in objs:
                print("** no instance found **")
                return
            print("** attribute missing **")
            return
        elif len(args) < 4:
            print("** value name missing **")
            return

        if obj_key in objs:
            setattr(objs[obj_key], args[2], args[3])
        else:
            print("** no instance found **")

    def emptyline(self):
        """Displays nothing"""
        pass

    def do_quit(self, arg):
        """ Quit the app"""
        return True

    def do_EOF(self, arg):
        """Quit the app with ctrl D"""
        return True


if __name__ == "__main__":
    my_cmd = HBNBCommand()
    my_cmd.cmdloop()
