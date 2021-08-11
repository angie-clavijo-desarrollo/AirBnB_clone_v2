#!/usr/bin/python3
"""State Module for HBNB project """
from sqlalchemy.sql.schema import Column
 from models.base_model import Base
from models.base_model import BaseModel
from sqlalchemy import Column, Integer, String
from sqlalchemy import create_engine


class DBStorage:
    """Class DBStorage """

if __name__ == "__main__":

    __engine = None
    __session = None

    def __init__(self):
        self.__engine = create_engine('mysql+mysqldb://HBNB_MYSQL_USER:\
                    HBNB_MYSQL_PWD@HBNB_MYSQL_HOST/\
                    HBNB_MYSQL_DB', ppool_pre_ping=True)
