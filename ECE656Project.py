import mysql.connector
from mysql.connector import errorcode
import pymysql
import argparse



def getDatabaseConnection(ipaddress, usr, passwd, charset, curtype): #obtained from https://pythontic.com/database/mysql/create%20user
    sqlCon  = pymysql.connect(host=ipaddress, user=usr, password=passwd, charset=charset, cursorclass=curtype)
    return sqlCon


def createUser(cursor, userName, password):
    try:
        sqlCreateUser = "CREATE USER '%s'@'localhost' IDENTIFIED BY '%s';" % (userName, password)
        cursor.execute(sqlCreateUser)
    except Exception as Ex:
        print("Error creating MySQL User: %s" % (Ex))


def login(user, password, IP):
    try:
        cnx = mysql.connector.connect(user=user, password=password, host=IP, database="ece656project")
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Incorrect user or password")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("Database does not exist")
        else:
            print(err)
    else:
        cnx.close()


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="To see which machine you're on...")
    parser.add_argument("--hammad", dest="machine", action="store_const", default=False)
    results = parser.parse_args()
    if results.machine:
        IP = "192.168.0.57"
    else:
        IP = "35.203.5.18"
    create = False if input("Create user?") == "no" else True
    user = input("Input username for database")
    password = input("Input password")
    if create:
        mySQLConnection = getDatabaseConnection(IP, "hammad", "hammadtrishal", "utf8mb4", pymysql.cursors.DictCursor)
        mySQLCursor = mySQLConnection.cursor()
        createUser(mySQLCursor, user, password)
    else: login(user, password, IP)

