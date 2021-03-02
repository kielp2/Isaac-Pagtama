from user import Contact
import mysql.connector
from mysql.connector import Error
import datetime
from datetime import date

#This function creates the connection
def create_connection(host_name,user_name, user_password, db_name):
    connector = None
    
    connection = mysql.connector.connect(
        host = host_name,
        user = user_name,
        passwd = user_password,
        database = db_name
    )

    print("Connection to MySQL DB successful")

    return connection

    #open up connection
#call funtion to open connection
connection = create_connection("ip-cis3368-db.cn1eadcsnzzp.us-east-1.rds.amazonaws.com","kielp2"
, "easyas123", "IsaacDB") #my database credentials needed to connect


def execute_read_query(connection, query):
    # cursor to operate
    cursor = connection.cursor()
    # variable to store results
    result = None
    try:
        cursor.execute(query)
        result = cursor.fetchall()
        return result
    except Error as e:
        print(f"The error '{e}' occurred")

     #executes a query
def execute_query(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        connection.commit()
        print("Query executed successfully")
    except Error as e:
        print(f"The error '{e}' occurred")


print("MENU: ")
print ("a - Add contact")
print("d - Remove contact")
print ("u - Update contact details")
print("b - Output all contacts in alphabetical order")
print ("c - Output all contacts by creation date")
print ("o - Output all contacts")
print ("q - Quit")
option = input()
print ("Choose an option: " + option)

