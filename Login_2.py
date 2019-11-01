import mysql.connector
from mysql.connector import Error
import Login_3
import Login_5

def check_user(cursor,user,password):
    username=user
    select_query="""SELECT * FROM login_details where username=%s"""
    cursor.execute(select_query,(username,))
    result_user=(cursor.fetchall())
    if result_user:
        cursor.execute("SELECT password FROM login_details where username=%s",(username,))
        result_pwd=cursor.fetchone()
        #print(result)
        if password in result_pwd:
            if Login_5.captcha():
                print("Login Successful")
            else:
                print("Invalid Captcha Value")
        else:
            print("Incorrect Password")
            cursor.execute("SELECT Secret_Question,Answer FROM login_details where username=%s",(username,))
            result=cursor.fetchone()
            print(result[0])
            user_answer=input("Enter the Answer:")
            if user_answer in result:
                print("Answer Accepted!\nChange Password link has been sent to your mail id!!")
            else:
                print("Incorrect Answer\nAccount has been linked")
    else:
        print("Username Not Found")
        print("Sign Up Below!")
        Login_3.Insert_New_User(cursor)


connection=mysql.connector.connect(host='localhost',user='root',password='root',database='login')
cursor=connection.cursor()
username=input("Enter the Username:")
password=input("Enter the password:")
check_user(cursor,username,password)

cursor.close()
connection.close()

