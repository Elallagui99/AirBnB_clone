#!/usr/bin/python3
"""

"""
import json
import os
from models.base_model import BaseModel
from models.user import User
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State


class FileStorage:
    """

    """
    __file_path = "file.json"
    __objects = {}

    def new(self, obj):
        """sets in __objects the obj with key <obj class name>.id"""
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        """serializes __objects to the JSON file (path: __file_path)"""
        objs = FileStorage.__objects
        obj_dict = {}
        for obj in objs.keys():
            obj_dict[obj] = objs[obj].to_dict()
        with open(FileStorage.__file_path, "w", encoding="utf-8") as file:
            json.dump(obj_dict, file)

    def reload(self):
        """deserializes the JSON file to __objects (only if the JSON file (__file_path) exists ;
          otherwise, do nothing. If the file doesn’t exist, no exception should be raised)"""
        with open(FileStorage.__file_path, 'r', encoding='utf-8') as file:
            try:
                obj_dict = json.loads(file)
                for key, value in obj_dict.items():
                    class_name, obj_id = key.split(".")
                    cls = eval(class_name)
                    obj = cls(**value)
                    FileStorage.__objects[key] = obj
            except Exception:
                pass

    def all(self):
        """ returns the dictionary __objects"""
        return FileStorage.__objects
