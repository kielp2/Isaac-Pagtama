from records import Contact
import mysql.connector
from mysql.connector import Error
import datetime
from datetime import date

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
        print(f"The error '{e}' occurred")

     #executes a query
def execute_query(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        connection.commit()
        print("Command Executed Successfully")
    except Error as e:
        print(f"The error '{e}' occurred")

#Prints menu for the user
print("MENU: ")
print ("a - Add contact")
print("d - Remove contact")
print ("u - Update contact details")
print("b - Output all contacts in alphabetical order")
print ("c - Output all contacts by creation date")
print ("o - Output all contacts")
print ("q - Quit")
print ("Choose an option: ")
option = input()

if option == "a":
    #CRUD - INSERT
    #Insert a new entry into the contacts table
    print("What is the full name?")
    name = input()
    print("What is his contact information? (Email or Phone Number Only)")
    contDetails = input()
    print("When was this record created? (yyyy-mm-ddd Format only)")
    createDate = input()

    query = "INSERT INTO contacts (Name, contactDetails, creationDate) VALUES ('%s', '%s', '%s')" % (name, contDetails, createDate,)
    execute_query(connection, query)
elif option == "d":
    # CRUD - Delete
    # delete an invoice entry from the invoice table
    print("Which ID would you like to completely delete? (Numbers only)")
    contact_delete = input()
    delete_statement = "DELETE FROM contacts WHERE id = %s" % (contact_delete)
    execute_query(connection, delete_statement)
elif option == "u":
    print("Press x to update the Name")
    print("Press y to update the Contact Description")
    print("Press z to update Creation Date")
    update = input()
    if update == "x":
        print("Which ID's name do you want to change? ") 
        id = input() #inputs the id of the name they want to change
        print("What will be the new name? ")
        new_name = input() #inputs the new name
        #SQL syntax that updates the name
        update_contact_query = """
        UPDATE
            contacts
        SET
            
            name = '%s'        
        

        WHERE
            id = %s  
        """ % (new_name, id)
        execute_query(connection, update_contact_query)
    elif update == "y":
        print("Which ID's Contact Description would you like to change?")
        id = input()
        print("What is the ID's new E-mail or Phone Number? ")
        new_details = input()
         #SQL syntax that updates the contact details
        update_contact_query = """
        UPDATE
            contacts
        SET
            
            contactDetails = '%s'
        

        WHERE
            id = %s  
        """ % (new_details, id)
        execute_query(connection, update_contact_query)
    elif update == "z":
        print("Which ID's creation date would you like to change? ")
        id = input()
        print("Enter the new date (Format: yyyy-mm-dd)")
        new_date= input()
         #SQL syntax that updates the creation date
        update_contact_query = """
        UPDATE
            contacts
        SET
            
            creationDate = '%s'
        
        WHERE
            id = %s  
        """ % (new_date, id)
        execute_query(connection, update_contact_query)
    else:
        print("Error: Command Not Found. Please Try Again")

        
elif option == "b":
    # read query - to get every row form the contacts table
    select_contacts = "SELECT * FROM contacts ORDER BY Name"
    # we are storing the result of our query
    contacts = execute_read_query(connection, select_contacts)

    # Making use of class Contact - parsing information from the result
    for contact in contacts:
        # create instance of class Contact and pass in the elements from result contact
        u = Contact(contact[0], contact[1], contact[2], contact[3])
        # now we use the field variables of class contact
        print("Name: " + u.Name)
        print("Contact Information: " + u.contactDetails)
        print("Date Created: " + str(u.createDate))
        print("--------------------------------")


elif option == "c":
    # read query - to get every row from the contacts table ordered by creationDates
    select_contacts = "SELECT * FROM contacts ORDER BY creationDate"
    # we are storing the result of our query
    contacts = execute_read_query(connection, select_contacts)

    # Making use of class User - parsing information from the result
    for contact in contacts:
        # create instance of class Contact and pass in the elements from result contact
        u = Contact(contact[0], contact[1], contact[2], contact[3])
        # now we use the field variables of class contact
        print("Name: " + u.Name)
        print("Contact Information: " + u.contactDetails)
        print("Date Created: " + str(u.createDate))
        print("--------------------------------")



elif option == "o":
    # read query - to get every row form the contacts table
    select_contacts = "SELECT * FROM contacts"
    # we are storing the result of our query
    contacts = execute_read_query(connection, select_contacts)

    # Making use of class Contact - parsing information from the result
    for contact in contacts:
        # create instance of class Conttact and pass in the elements from result contact
        u = Contact(contact[0], contact[1], contact[2], contact[3])
        # now we use the field variables of class contact
        print("Name: " + u.Name)
        print("Contact Information: " + u.contactDetails)
        print("Date Created: " + str(u.createDate))
        print("---------")

elif option == "q":
    print ("Program Has Quit")
    quit()

else:
    print("Error: Unkown Command. Please Try Again")






    
    

    
    

