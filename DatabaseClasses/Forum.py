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
        cursor = cnx.cursor()
        threads = []
        query = ("SELECT thread_id FROM threads "
                 f"WHERE forum_id = {self.forum_id}")
        cursor.execute(query)
        for (thread_id) in cursor:
            threads.append(thread_id)
        return threads

    def getContributors(self, cnx: mysql.connector.connect()):
        cursor = cnx.cursor()
        contributors = []
        query = ("SELECT contributor_id FROM contributors "
                 f"WHERE forum_id = {self.forum_id}")
        cursor.execute(query)
        for (contributor_id) in cursor:
            contributors.append(contributor_id)
        return contributors

    def getPosts(self, cnx: mysql.connector.connect()):
        cursor = cnx.cursor()
        posts = []
        for (thread_id) in self.threads:
            query = ("SELECT post_id FROM posts "
                     f"WHERE thread_id = {thread_id} "
                     f"AND user_id = {self.user_id}")
            cursor.execute(query)
            for (post_id) in cursor:
                posts.append(post_id)
        return posts

    def updateThreads(self, additionalThreads, cnx: mysql.connector.connect()):
        cursor = cnx.cursor()
        queries = []
        for thread in additionalThreads:
            addToQuery = f"({thread}, {self.forum_id})"
            queries.append(addToQuery)
        query = "INSERT INTO threads" "(thread_id, forum_id) " "VALUES "
        for i in range(len(queries)):
            if i == len(queries) - 1:
                query += queries[i]
            else:
                query += queries[i] + ", "
        cursor.execute(query)

    def updateContributors(self, additionalContributors, cnx:mysql.connector.connect()):
        cursor = cnx.cursor()
        queries = []
        for contributor in additionalContributors:
            addToQuery = f"({self.forum_id}, {contributor})"
            queries.append(addToQuery)
        query = "INSERT INTO contributors" "(forum_id, contributor_id) " "VALUES "
        for i in range(len(queries)):
            if i == len(queries) - 1:
                query += queries[i]
            else:
                query += queries[i] + ", "
        cursor.execute(query)

    def updatePosts(self, additionalPosts, cnx:mysql.connector.connect()):
        cursor = cnx.cursor()
        queries = []
        for post in additionalPosts:
            addToQuery = f"({post}, {self.thread_id}, {self.user_id}, "test")"
            queries.append(addToQuery)
        query = "INSERT INTO contributors" "(post_id, thread_id, user_id, post) " "VALUES "
        for i in range(len(queries)):
            if i == len(queries) - 1:
                query += queries[i]
            else:
                query += queries[i] + ", "
        cursor.execute(query)