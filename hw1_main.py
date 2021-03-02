from user import Contact
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

    # nice function to execute a query
def execute_query(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        connection.commit()
        print("Query executed successfully")
    except Error as e:
        print(f"The error '{e}' occurred")




#CRUD - Read
# read query - to get every row form the users table
select_users = "SELECT * FROM contacts"
# we are storing the result of our query
users = execute_read_query(connection, select_users)

print(users)

# Making use of class User - parsing information from the result
for contact in users:
    # create instance of class User and pass in the elements from result users
    u = Contact(contact[0], contact[1], contact[2], contact[3])
    # now we use the field variables of class user
    print(u.Name)
    print(u.contactDetails)
    print(u.createDate)
    print("-------")
'''
#CRUD - UPDATE
#Insert a new entry into the users table
name = input()
contDetails = input()
createDate = input()

query = "INSERT INTO contacts (Name, contactDetails, creationDate) VALUES ('%s', '%s', '%s')" % (name, contDetails, createDate,)
execute_query(connection, query)

# CRUD - Delete
# delete an invoice entry from the invoice table
contact_delete = input()
delete_statement = "DELETE FROM contacts WHERE id = %s" % (contact_delete)
execute_query(connection, delete_statement)
'''

# update a record
'''
new_details = input()

id = input()
update_contact_query = """
UPDATE
    contacts
SET
    
    contactDetails = '%s'
   

WHERE
    id = %s  
""" % (new_details, id)
execute_query(connection, update_contact_query)

new_name = input()

id = input()
update_contact_query = """
UPDATE
    contacts
SET
    
    name = '%s'
   

WHERE
    id = %s  
""" % (new_name, id)
execute_query(connection, update_contact_query)
'''



new_date= input()

id = input()
update_contact_query = """
UPDATE
    contacts
SET
    
    creationDate = '%s'
   
WHERE
    id = %s  
""" % (new_date, id)
execute_query(connection, update_contact_query)