import mysql.connector

def db_Connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="Siri@2025",
        database="HDFCBank"
    )
print("db connected successfully.....") 