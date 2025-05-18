# db_config.py
import mysql.connector   # a channel to connect python code to database


db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="777888",
) 

cursor = db.cursor() # Execute raw SQL
cursor.execute("CREATE DATABASE crm_db")

print('db connect succesfully')