import mysql.connector
from mysql.connector import errorcode
import pymysql
from DatabaseClasses.AbstractClasses import DataBaseObject


class User(DataBaseObject):
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

    def updateInDatabase(self, cnx: mysql.connector.connect()):
        cursor = cnx.cursor()
        update_user = ("UPDATE users "
                       "SET first_name = %s, last_name = %s, birth_date= %s"
                       f"WHERE user_id = {self.userID}")
        first_name = self.firstName
        last_name = self.lastName
        birth_date = self.birthDate
        cursor.execute(update_user, (first_name, last_name, birth_date))
        cursor.close()
        oldFriends = self.getFriends(cnx)
        additionalFriends = list(set(self.friends) - set(oldFriends))
        self.updateFriends(additionalFriends, cnx)



    def createInDatabase(self, cnx: mysql.connector.connect()):
        cursor = cnx.cursor()
        add_user = ("INSERT INTO users "
                    "(user_id, first_name, last_name, birth_date)"
                    "VALUES (%s, %s, %s, %s)")
        data_user = (self.userID, self.firstName, self.lastName, self.birthDate)
        cursor.execute(add_user, data_user)
        cnx.commit()
        cursor.close()
        self.updateFriends(self.friends, cnx)


    def checkDatabaseExistence(self, cnx: mysql.connector.connect()):
        cursor = cnx.cursor()
        query = ("SELECT user_id FROM users "
                 f"WHERE user_id = {self.userID}")
        cursor.execute(query)
        for (userID) in cursor:
            if userID:
                return True

    def getFriends(self, cnx: mysql.connector.connect()):
        cursor = cnx.cursor()
        friends = []
        query = ("SELECT friend_id FROM connections "
                 f"WHERE user_id = {self.userID}")
        cursor.execute(query)
        for (friend_id) in cursor:
            friends.append(friend_id)
        return friends

    def updateFriends(self, additionalFriends, cnx: mysql.connector.connect()):
        cursor = cnx.cursor()
        queries = []
        for friend in additionalFriends:
            addToQuery = f"({self.userID}, {friend})"
            queries.append(addToQuery)
        query = "INSERT INTO connections" "(user_id, friend_id)" "VALUES "
        for i in range(len(queries)):
            if i == len(queries) - 1:
                query += queries[i]
            else:
                query += queries[i] + ", "
        cursor.execute(query)


