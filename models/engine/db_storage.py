#!/usr/bin/python3
""" State Module for HBNB project """
from os import getenv
from models.base_model import Base
from models.base_model import BaseModel
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User
from sqlalchemy import create_engine
from sqlalchemy.orm import relationship
from sqlalchemy.orm import scoped_session
from sqlalchemy.orm import sessionmaker


class DBStorage:
    """Class DBStorage """

if __name__ == "__main__":

    __engine = None
    __session = None

    def __init__(self):
        self.__engine = create_engine('mysql+mysqldb://HBNB_MYSQL_USER:\
                    HBNB_MYSQL_PWD@HBNB_MYSQL_HOST/\
                    HBNB_MYSQL_DB', ppool_pre_ping=True)
