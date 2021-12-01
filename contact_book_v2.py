<<<<<<< HEAD
def user_choice(user_args):
    user_input = input("Choose one of the following:\n[C] - Create a new contact\n[D] - Delete an existing contact\n[A] - Show all saved contacts\n[F] - Seach contact\n").upper()
    if user_args == "C":
        return create_contact(user_args)
    elif user_args == "D":
        print("Delete contact")
    elif user_args == "A":
        print("Show all contacts")
    elif user_args == "F":
        print("Search contact")
    else:
        print("Error! Not a valid option.")
        print("Choose one of the following:\n[C] - Create a new contact\n[D] - Delete an existing contact\n[A] - Show all saved contacts\n[F] - Seach contact")
        another_attemp = input()
        return user_choice(another_attemp)


def create_contact(user_args):
    contact_dict = {}
    first_name = input()
    last_name = input()
    phone_number = input()
    contact_dict[first_name, last_name] = phone_number
    
    return user_choice(user_args)
    

user_choice(None)
=======
import fileinput
import re

def action(choice):
    user_input = input("Select one of the following operations:\n[C] - Create a new contact\n[A] - Show all contacts\n[S] - Search for a contact\n[D] - Delete contact\n[X] - Exit\n").upper()
    if user_input == "C":
        print("Create new contact.")
        return create_contact(user_input)
    elif user_input == "D":
        print("Delete an existing contact.")
        return delete_contact(user_input)
    elif user_input == "A":
        print("Show all contacts.")
    elif user_input == "S":
        print("Search for a specific contact.")
    elif user_input == "X":
        print("Thank you for using the app!")
        return 0
    else:
        print("Error! Unknown choice")
        return action(None)
    return action(None)

def create_contact(new_contact):
    first_name = input("Enter the first name:\n")
    last_name = input("Enter the last name:\n")
    phone_number = input("Enter the phone number:\n")
    contacts = {}
    contacts[first_name, last_name] = phone_number
    file = open('contacts.txt', 'a')
    file.write(f"Contact name: {first_name} >>> {last_name}. Contact phone number: {phone_number} \n\n###########################\n\n")
    file.close()
    return action(None)


def delete_contact(contact):
    contact_name = input("Enter a contact name to delete:\n")
    with open('contacts.txt', 'r+') as file:
        lines = file.readlines()
        for _ in range(len(lines)):
            current_object = lines[_]
            if contact_name in current_object:
                lines.remove(current_object)
                file.truncate(_)
                for element in lines:
                    file.write(element)
                file.close()
                break
                    
action(None)
>>>>>>> 3122561fda593298a6f41f0f7ff91bc1bd7e200d
