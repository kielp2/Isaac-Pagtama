import mysql.connector
from mysql.connector import Error
import datetime
from datetime import date
import requests
import simplejson as json


#This function creates the connection to the database
def create_connection(host_name,user_name, user_password, db_name):
    connector = None
    
    connection = mysql.connector.connect( #this python code connects to MYSQL Server
        host = host_name,
        user = user_name,
        passwd = user_password,
        database = db_name
    )

    print("Program Has Connected To Database") #Verifies that the connection is successful

    return connection #returns the connection

    #open up connection
#call funtion to open connection
connection = create_connection("ip-cis3368-db.cn1eadcsnzzp.us-east-1.rds.amazonaws.com","kielp2"
, "easyas123", "IsaacDB") #my database credentials needed to connect


def execute_read_query(connection, query):
    # cursor to operate
    cursor = connection.cursor()
    # variable to store results
    result = None
    try: #a try and except that statement for validation
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
        print("Data Has Been Stored Into The Database")
    except Error as e:
        print(f"The error '{e}' occurred") #only prints if there are connection errors


response = requests.get("https://api.covidtracking.com/v1/states/daily.json") #the get method sends a get request to the URL

json_test = response.json() #declares the variable json_test to response.json

print("Enter the state for which the COVID data should be retrieved (e.g. TX): ")
user_state = input() #asks the user to input a state abbreviation
print("Enter the date for which the COVID data should be retrieved (e.g. 20201219): ")
user_date = input() #asks the user to input a date in a yyymmdd format
status = False #creates a boolean for the variable status


count = 0 #declares count a 0 starting point for the for-loop
for i in json_test: #for-loop that searches the data inside the .json url
    i = count #declares i as count
    count = count + 1 #once the for-loop loops once, it adds 1 to count and restarts the loop
    state = (json_test[i]['state'])            
    dates = (json_test[i]['date'])        #these variables are declared to its designated data      
    death = (json_test[i]['death'])         #inside the json file
    positive = (json_test[i]['positive'])   
    positiveIncrease = (json_test[i]['positiveIncrease'])
    deathIncrease = (json_test[i]['deathIncrease'])

    if state == user_state and str(dates) == user_date: #if statement that validates the user input data
        status = True #boolean statement saying that the if statement is True
        cv_state = state #declares cv_state as state
        cv_date = dates   #declares cv_date as date          
        cv_death = death    #declares cv_death as death
        cv_positive = positive #declares cv_positive as positive
        cv_positiveIncrease = positiveIncrease #declares cv_positiveIncrease as positiveIncrease
        cv_deathIncrease = deathIncrease #declares cv_deathIncrease as deathIncrease
        #The following print statements prints the data pulled from the user input
        print(" ")
        print("=======================") 
        print("State: " + str(cv_state)) #prints the state that the user inputted        
        print("Date: " + str(cv_date)) #prints the date that the user inputted
        print("Positive Cases: " + str(cv_positive)) #prints the number of positive cases in the selected the state and date
        print("Death(s): " + str(cv_death)) #prints the number of deaths in the selected state and date
        print("=======================")
        print(" ")


        cvstate = cv_state #declares cvstate as cv_state
        cvdate = cv_date  #declares cvdate as cv_date
        cvdeath = cv_death #declares cvdeath as cv_death
        cvpositive = cv_positive #declares cvpositive as cv_positive
        cvpositiveIncrease = cv_positiveIncrease #declares cvpositiveIncrease as cv_positiveIncrease
        cvdeathInrease = cv_deathIncrease #declares cvdeathInrease as cv_deathIncrease
        query = "INSERT INTO exam1 (state, date, positive, deaths, positiveIncrease, deathIncrease) VALUES ('%s', '%s', '%s', '%s', '%s', '%s')" % (cvstate, cvdate, cv_death, 
        cv_positive, cv_positiveIncrease, cv_deathIncrease) #the code stores the data from the user input into the exam1 table in MYSQL database
        execute_query(connection, query) #executes the query
if(status==False): #this if statement prints "No Records Were Found. Please Try Again" if the boolean is falsee
    print("No Records Were Found. Please Try Again")