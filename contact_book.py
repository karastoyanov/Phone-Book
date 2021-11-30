import pickle


contact_book = {}


while True: 
    user_choice = input("Select one of the following operations: \n [C] - Create a new contact \n [A] - Show all contacts" 
                        "\n [S] - Search for a contact \n [D] - Delete contact \n [X] - Exit \n").upper()
    
    if user_choice == "C":
        contact_name = input()
        contact_number = input()
        # contact_book[contact_name] = contact_number 
        fout = "phone_book.txt"
        fo = open(fout, "a+")
        # Put the cursor at the begging of the file
        fo.seek(0) 
        # If the file is not empty, then append new blank line
        data = fo.read(100) 
        for k in contact_name:
            if len(data) > 0:
                fo.write("\n")
            fo.write(str(contact_name) + " >>> ")
            break
        for v in contact_number:
            fo.write(str(contact_number))
            print(f"{contact_name} was saved in the contact list.")
            contact_number = ''
            contact_name = ''
            break
   
    if user_choice == "A":
        
        
        
    if user_choice == "S":
        search_name = input("Enter a contact name: ")
        if search_name in contact_book:
            print(f'{search_name} has been found in contact list. {search_name} phone number is {contact_book.get(contact_name)}')
        else: 
            print(search_name, "is not found in the contact list.")
    
    
    if user_choice == "D":
        contact_to_delete = input("Enter the contact name you would like to delete: ")
        if contact_to_delete in contact_book:
            contact_book.pop(contact_to_delete)
            print(f"{contact_to_delete} was removed from the contact list.")
        else:
            print(f"{contact_to_delete} has not been found.")
    
    
    if user_choice == "X":
        break
