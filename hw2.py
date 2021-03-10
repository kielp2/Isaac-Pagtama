import mysql.connector
from mysql.connector import Error
import datetime
from datetime import date
import requests
import simplejson as json

#This function creates the connection to the database
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
        print(f"The error '{e}' occurred") #only prints if there are connection errors

     #executes a query
def execute_query(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        connection.commit()
        print("Command Executed Successfully")
    except Error as e:
        print(f"The error '{e}' occurred") #only prints if there are connection errors




response = requests.get("https://projects.propublica.org/nonprofits/api/v2/search.json")

json_test = response.json()


count = 0
for i in json_test:
    i = count
    count = count + 1
    org_name = (json_test['organizations'][2]['name'])
    org_city = (json_test['organizations'][2]['city'])
    org_state = (json_test['organizations'][2]['state'])

    #print(org_name + ", " + org_city + ", " + org_state)

print("enter input")
(x) = input()
org_name = (json_test['organizations'][int(x)]['name'])
org_city = (json_test['organizations'][int(x)]['city'])
org_state = (json_test['organizations'][int(x)]['state'])
    
print(org_name + ", " + org_city + ", " + org_state)


#CRUD - INSERT
    #Insert a new entry into the results table
 
name = org_name
    
city = org_city
    
state = org_state

query = "INSERT INTO results (name, city, state) VALUES ('%s', '%s', '%s')" % (name, city, state,)
#execute_query(connection, query)

