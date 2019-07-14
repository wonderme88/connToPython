
import MySQLdb


# Open database connection
db = MySQLdb.connect("localhost","root","Root123#","TUTORIALS" )


# prepare a cursor object using cursor() method
cursor = db.cursor()

# Prepare SQL query to INSERT a record into the database.
sql = """INSERT INTO STUDENTS_REC(STU_ID,STU_NAME,STU_GRADE,
       STU_STREAM )
         VALUES (02,"RISHUB PUNT",11,"ARTS")"""


cursor.execute(sql)
db.commit()

#FIRST_NAME = "birender"
#LAST_NAME = "singh"
#AGE=37
#SEX="M"
#INCOME=3000

                            
