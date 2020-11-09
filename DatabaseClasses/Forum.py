import mysql.connector
from mysql.connector import errorcode
import pymysql
from DatabaseClasses.AbstractClasses import DataBaseObject

class Forum(DataBaseObject):
    def __init__(self, forum_id, title_id, contributors=None, threads=None, posts=None):
        self.forum_id = forum_id
        self.title_id = title_id
        if contributors:
            self.contributors = contributors
        if threads:
            self.threads = None
        if posts:
            self.posts = None

    def updateInDatabase(self, cnx: mysql.connector.connect()): #what about removals?
        cursor = cnx.cursor()
        update_user = ("UPDATE forum "
                       "SET forum_id = %s, titleID = %s"
                       f"WHERE forum_id = {self.forum_id}")
        cursor.execute(update_user, (self.forum_id, self.title_id))
        cursor.close()
        if self.threads:
            oldThreads = self.getThreads(cnx)
            additionalThreads = list(set(self.threads) - set(oldThreads))
            self.updateThreads(additionalThreads, cnx)
        if self.contributors:
            oldContributors = self.getContributors(cnx)
            additionalContributors = list(set(self.contributors) - set(oldContributors))
            self.updateContributors(additionalContributors, cnx)
        if self.posts:
            oldPosts = self.getPosts(cnx)
            additionalPosts = list(set(self.posts) - set(oldPosts))
            self.updatePosts(additionalPosts, cnx)

    def createInDatabase(self, cnx: mysql.connector.connect()):
        cursor = cnx.cursor()
        add_forum = ("INSERT INTO forum "
                    "(forum_id, titleID)"
                    "VALUES (%s, %s)")
        data_forum = (self.forum_id, self.title_id)
        cursor.execute(add_forum, data_forum)
        cnx.commit()
        cursor.close()
        if self.contributors:
            self.updateContributors(self.contributors, cnx)
        if self.threads:
            self.updateThreads(self.threads, cnx)
        if self.posts:
            self.updatePosts(self.posts, cnx)

    def checkDatabaseExistence(self, cnx: mysql.connector.connect()):
        cursor = cnx.cursor()
        query = ("SELECT forum_id FROM forum "
                 f"WHERE forum_id = {self.forum_id}")
        cursor.execute(query)
        for (forum_id) in cursor:
            if forum_id:
                return True
        return False

    def getThreads(self, cnx: mysql.connector.connect()):
        pass

    def getContributors(self, cnx: mysql.connector.connect()):
        pass

    def getPosts(self, cnx: mysql.connector.connect()):
        pass

    def updateThreads(self, additionalThreads, cnx: mysql.connector.connect()):
        pass

    def updateContributors(self, additionalContributors, cnx:mysql.connector.connect()):
        pass

    def updatePosts(self, additionalPosts, cnx:mysql.connector.connect()):
        pass