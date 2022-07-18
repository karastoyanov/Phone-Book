def main(*args):
    while True:
        print('Press 1 to create a new contact\nPress 2 to save the contact')
        user_action = int(input("Enter your choice:\n"))
        
        if user_action == 1:
            import create_new_contact
            break
        elif user_action == 2:
            import save_contact
            break
        else:
            print("Choose a valid option")
            continue

if __name__ == '__main__':
    main()