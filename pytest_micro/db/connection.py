import mysql.connector


def get_connection():

    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="23UEEC0536@h",   
        database="university_db"
    )

    return conn