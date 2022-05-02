import random

class Contact:
    def __init__(self, firstName, lastName, mobilePhone: str, emailAdrress, companyName, idNumber : str):
        self.firstName = firstName
        self.lastName = lastName
        self.mobilePhone = mobilePhone
        self.emailAdrress = emailAdrress
        self.companyName = companyName
        self.idNumber = idNumber
    
    def save_contact(self):
        pass
    
    
    def __repr__(self):
        return self.firstName + ' ' + self.lastName + '\n' + self.mobilePhone + \
            '\n' + self.emailAdrress + '\n' + self.companyName + '\n' + self.idNumber
        

# contact_one = Contact("Ivan", "Ivanov", '555-666', 'i.ivanov@gmail.com', "Sales Ltd.", '1')
# contact_two = Contact("Georgi", "Georgiev", '555-777', 'georgiev@gmail.com', "GG Ltd.", '2')
# print(contact_one.__repr__())