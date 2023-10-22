#!/usr/bin/python3
"""This script is the base model"""

<<<<<<< HEAD
=======
from datetime import datetime
#!/usr/bin/python3
"""Module for Base class
Contains the Base class for the AirBnB clone console.
"""

>>>>>>> 2866708bb8204326d9b1425868ef64a7c2a2bdc9
import uuid
from datetime import datetime
from models import storage


class BaseModel:

<<<<<<< HEAD
    """Class from which all other classes will inherit"""

    def __init__(self, *args, **kwargs):
        """Initializes instance attributes
=======
    """Class for base model of object hierarchy."""

    def __init__(self, *args, **kwargs):
        """Initialization of a Base instance.
>>>>>>> 2866708bb8204326d9b1425868ef64a7c2a2bdc9

        Args:
            - *args: list of arguments
            - **kwargs: dict of key-values arguments
        """

        if kwargs is not None and kwargs != {}:
            for key in kwargs:
                if key == "created_at":
                    self.__dict__["created_at"] = datetime.strptime(
                        kwargs["created_at"], "%Y-%m-%dT%H:%M:%S.%f")
                elif key == "updated_at":
                    self.__dict__["updated_at"] = datetime.strptime(
                        kwargs["updated_at"], "%Y-%m-%dT%H:%M:%S.%f")
                else:
                    self.__dict__[key] = kwargs[key]
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)

    def __str__(self):
<<<<<<< HEAD
        """Returns official string representation"""
=======
        """Returns a human-readable string representation
        of an instance."""
>>>>>>> 2866708bb8204326d9b1425868ef64a7c2a2bdc9

        return "[{}] ({}) {}".\
            format(type(self).__name__, self.id, self.__dict__)

    def save(self):
<<<<<<< HEAD
        """updates the public instance attribute updated_at"""
=======
        """Updates the updated_at attribute
        with the current datetime."""
>>>>>>> 2866708bb8204326d9b1425868ef64a7c2a2bdc9

        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
<<<<<<< HEAD
        """returns a dictionary containing all keys/values of __dict__"""
=======
        """Returns a dictionary representation of an instance."""
>>>>>>> 2866708bb8204326d9b1425868ef64a7c2a2bdc9

        my_dict = self.__dict__.copy()
        my_dict["__class__"] = type(self).__name__
        my_dict["created_at"] = my_dict["created_at"].isoformat()
        my_dict["updated_at"] = my_dict["updated_at"].isoformat()
        return my_dict
