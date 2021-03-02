#A class meant for main.py
#classes are used to create user-defined data structures
#classes can also define funtions called methods, which identify the
#actions that an object created from the class can perform with its

#Python class names are written in Capitalized words
class Contact:
    def __init__(self, id, Name, contactDetails, createDate):
        self.id = id
        self.Name = Name
        self.contactDetails = contactDetails
        self.createDate = createDate