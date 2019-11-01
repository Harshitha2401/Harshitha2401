import mysql.connector
from mysql.connector import Error

def creation(cursor):
    database_creation="""CREATE DATABASE Login"""
    cursor.execute(database_creation)
    cursor.execute("USE Login")
    table_creation="""CREATE TABLE Login_Details(Username VARCHAR(255) PRIMARY KEY,Password VARCHAR(255),Secret_Question VARCHAR(255),Answer VARCHAR(255))"""
    cursor.execute(table_creation)

def insertion(connection,username,password,question,answer):
    cursor=connection.cursor()
    insert_query="""INSERT INTO Login_Details(Username,Password,Secret_Question,Answer) VALUES (%s,%s,%s,%s)"""
    record_tuple=(username,password,question,answer)
    cursor.execute(insert_query,record_tuple)
    cursor.execute("COMMIT")

connection=mysql.connector.connect(host='localhost',user='root',password='root')
cursor=connection.cursor()
#except:
    #print("Failed to connect")
    #exit(0)

creation(cursor)
while True:
    username=input("Enter the username:")
    password=input("Enter the password:")
    question=input("Enter the question:")
    answer=input("Enter the answer:")
    insertion(connection,username,password,question,answer)
    ch=input("Do you need to enter another record:(Y/N)")
    if ch=='N' or ch=='n':
        break

cursor.close()
connection.close()






