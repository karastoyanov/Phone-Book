import create_new_contact as cnc

def save_contact():
    file1 = open("conctact.txt", 'w')
    file1.write(f'cnc.first_name + \n + cnc.last_name + \n + cnc.email + \n + cnc.phone')
    file1.close()

save_contact()