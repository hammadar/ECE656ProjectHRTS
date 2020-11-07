import mysql.connector
from mysql.connector import errorcode
import pymysql

class User:
    def __init__(self, userID, firstName, lastName, birthDate, location=None, friends=None):
        self.userID = userID
        self.firstName = firstName
        self.lastName = lastName
        self.birthDate = birthDate
        if location:
            self.location = location
        if friends:
            self.friends = friends

    def addFriend(self, friendID):
        if self.friends:
            self.friends.append(friendID)
        else:
            self.friends = [friendID]

    def updateDatabase(self, user, password):
        cnx = mysql.connector.connect(user=user, password=password, host="35.203.5.18", database="ece656project")
        cursor = cnx.cursor()
        #update_text = ""
        update_user = ("UPDATE users "
                       "SET first_name = %s, last_name = %s, birth_date= %s"
                       f"WHERE user_id = {self.userID}")
        first_name = self.firstName
        last_name = self.lastName
        birth_date = self.birthDate
        cursor.execute(update_user, (first_name, last_name, birth_date))
        cursor.close()
        cnx.close()