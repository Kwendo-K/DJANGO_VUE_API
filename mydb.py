"""
creating mysql database using python
"""
import mysql.connector

database = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="Mysql@1991",
)

cursorObject = database.cursor()
cursorObject.execute("CREATE DATABASE Django_Api")
print("Database created successfully")