import mysql.connector
from mysql.connector import Error
import datetime
from datetime import date

#we want to write a funtion that handles creation of connection
def create_connection(host_name,user_name, user_password, db_name):
    connector = None
    #wrap the following into a try except statement
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
, "easyas123", "IsaacDB")

