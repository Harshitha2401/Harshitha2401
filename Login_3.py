import mysql.connector
from mysql.connector import Error
import Login_4
import Login_6

def Insert_New_User(cursor):
    username=input("Enter the Username:")
    password=input("Enter the Password:")
    secret_question=input("Enter the Secret Question:")
    answer=input("Enter the Answer:")
    email_id=input("Enter the Email-ID:")
    if Login_4.pwd_valid(password):
        if Login_6.email_validation(email_id):
            sql_record=(username,password,secret_question,answer,email_id)
            insert_query = """INSERT INTO Login_Details(Username,Password,Secret_Question,Answer,email_id) VALUES (%s,%s,%s,%s,%s)"""
            cursor.execute(insert_query,sql_record)
            cursor.execute("COMMIT")
            print("Account created Successfully!")
        else:
            print("Email Criteria not matching")
    else:
        print("Password criteria not matching")