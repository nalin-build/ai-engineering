import json

def main():
    contacts = {}
    file_name = input("please enter the file name without .json : ").strip()
    file_name = file_name + '.json'
    try:
        with open(file_name, 'r') as file:
            contacts = json.load(file)
            print("these are all the contacts present currently in the dictionary -_-")
            print(contacts)

    except FileNotFoundError:
        print("the file was not found, will create a new one to add contacts in -_-")
        pass
    
    while True:
        name = input("please enter the name you would like to add/edit or enter done to exit: ").strip().lower()
        if name == 'done':
            break
        
        if name in contacts:
            option = input(f"the {name} is already present in contacts are you sure you want to edit it enter y/n : ").strip().lower()
            if option != 'y':
                continue

        if name not in contacts:
            contacts[name] = {}

        while True:
            try:
                phone = int(input(f"please enter the phone number of {name} : ").strip())
                contacts[name]['phone'] = phone
                break
            except ValueError:
                print("please enter a valid phone number -_-")
               

        email = input(f"please enter the email of {name} : ")
        contacts[name]['email'] = email

    with open(file_name, 'w') as file:
        json.dump(contacts, file, indent = 2)
            
            











main()