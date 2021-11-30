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