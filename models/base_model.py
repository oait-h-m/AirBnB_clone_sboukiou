#!/usr/bin/python3
"""
Base model for all classes
"""

import uuid
import datetime
import json
from datetime import datetime


class BaseModel():
    """
    Base model
    """

    def __init__(self):
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __str__(self):
        """
        Class string presentation
        """
        return "[{}] ({}) {}".format(self.__class__.__name__,
                                     self.id, self.__dict__)

    def save(self):
        """
        Updates the time to last update
        """
        self.updated_at = datetime.now()

    def to_dict(self):
        """
        Saves class info into a dictionary
        """
        class_dict = {}
        for element in self.__dict__:
            class_dict[element] = self.__dict__[element]
        class_dict["__class__"] = self.__class__.__name__
        class_dict["created_at"] = self.created_at.isoformat()
        class_dict["updated_at"] = self.updated_at.isoformat()
        return class_dict
