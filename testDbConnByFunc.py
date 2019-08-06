#!/usr/bin/python

import MySQLdb

def getDbConnection():
	# Open database connection
	try:
		connection = MySQLdb.connect("localhost","root","Root123#","TUTORIALS" )
		print("Connection Done!!")
		return connection
		
	except MySQLdb.Error as e:
		print("Failed to connect to database {}".format(error))

def closeDbConnection(connection):
	#Close Database connection
	try:
		connection.close()
		print("Close Database connection Done!!!")
	except MySQLdb.Error as e:
		print("Failed to close the database {}".format(error))

def readDbVersion():
    try:
        connection = getDbConnection()
        db_Info = connection.get_server_info()
        print("Connected to MySQL database... MySQL Server version is ", db_Info)
        cursor = connection.cursor()
        cursor.execute("select database();")
        record = cursor.fetchone()
        print("Your connected to - ", record)
        closeDbConnection(connection)
    except MySQLdb.Error as e:
        print("Failed to read database version {}".format(error))

print("Start of a Python Database Programming Exercise\n")
		
readDbVersion()

