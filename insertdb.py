#!/usr/bin/python

import MySQLdb


# Open database connection
db = MySQLdb.connect("localhost","root","Root123#","TUTORIALS" )


# prepare a cursor object using cursor() method
cursor = db.cursor()

# Prepare SQL query to INSERT a record into the database.
#sql = """INSERT INTO EMPLOYEE(FIRST_NAME,
#         LAST_NAME, AGE, SEX, INCOME)
#         VALUES ('Mac', 'Mohan', 20, 'M', 2000)"""

#FIRST_NAME = "birender"
#LAST_NAME = "singh"
#AGE=37
#SEX="M"
#INCOME=3000

print('Enter your first name:')
FIRST_NAME = raw_input()
print('Hello, ' + FIRST_NAME)


print('Enter your last name:')
LAST_NAME = raw_input()
print('Hello, ' +FIRST_NAME+ LAST_NAME)

print('Enter your age:')
AGE = int(raw_input())
print('AGE ' + str(AGE))

print('Enter your sex:')
SEX = raw_input()
print('SEX ' + SEX)

print('Enter your income:')
INCOME = int(raw_input())
print('INCOME ' + str(INCOME))







sql = "INSERT INTO EMPLOYEE(FIRST_NAME, \
       LAST_NAME, AGE, SEX, INCOME) \
       VALUES ('%s', '%s', '%d', '%c', '%d' )" % \
       (FIRST_NAME, LAST_NAME,AGE, SEX, INCOME)


# Prepare SQL query to INSERT a record into the database.
#sql = "INSERT INTO EMPLOYEE(FIRST_NAME, \
#       LAST_NAME, AGE, SEX, INCOME) \
#       VALUES ('%s', '%s', '%d', '%c', '%d' )" % \
#       ('Mac', 'Mohan', 20, 'M', 2000)




try:
   # Execute the SQL command
   cursor.execute(sql)
   # Commit your changes in the database
   db.commit()
except:
   # Rollback in case there is any error
   db.rollback()





cursor.execute(sql)

# disconnect from server
db.close()



