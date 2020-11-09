import mysql.connector
from mysql.connector import errorcode
import pymysql
from abc import ABC, abstractmethod

class DataBaseObject(ABC):
    @abstractmethod
    def updateInDatabase(self, cnx: mysql.connector.connect()):
        pass
    @abstractmethod
    def createInDatabase(self, cnx: mysql.connector.connect()):
        pass
    @abstractmethod
    def checkDatabaseExistence(self, cnx: mysql.connector.connect()):
        pass

