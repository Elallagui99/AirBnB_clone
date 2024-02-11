#!/usr/bin/python3
"""
contains class BaseModel
"""
import uuid
from datetime import datetime
import models


class BaseModel:
    """ BaseModel class from which future classes will inherite """

    def __init__(self, *arg, **kwargs):
        """ initialization """
        time_iso_format = "%Y-%m-%dT%H:%M:%S.%f"
        self.id = str(uuid.uuid4())

        self.created_at = datetime.utcnow()
        self.updated_at = datetime.utcnow()
        if (kwargs):
            for key, value in kwargs.items():
                if key == "__class__":
                    continue
                elif key == "created_at" or key == "updated_at":
                    setattr(self, key, datetime.strptime(
                        value, time_iso_format))
                else:
                    setattr(self, key, value)

        models.storage.new(self)

    def save(self):
        """update attribute with current datetime """
        self.updated_at = datetime.utcnow()
        models.storage.new(self)
        models.storage.save()

    def to_dict(self):
        """return a dictinary contains all keys and values on instance """
        my_dict = self.__dict__.copy()
        my_dict["__class__"] = self.__class__.__name__
        my_dict["created_at"] = self.created_at.isoformat()
        my_dict["updated_at"] = self.updated_at.isoformat()
        return my_dict

    def __str__(self):
        """ string representation of basemodel class """
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def delete(self):
        """ delete the current instance from the storage """
        models.storage.delete(self)


if __name__ == "__main__":
    my_model = BaseModel()
    my_model.name = "First Model"
    my_model.my_number = 66
    print(my_model)
    my_model.save()
    print(my_model)
    my_model_json = my_model.to_dict()
    print(my_model_json)
