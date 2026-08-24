def add_or_edit_contact(contact, name, phone , email ):
    while True:
        if name in contact:
            option = input("""the user already exists, do you wish to edit the contact information of the user
            Type yes/no  >>>>> """).lower().strip()
            if option == "no":
                return
            elif option == "yes":
                contact[name]["phone"] = phone
                contact[name]["email"] = email
                return
            else:
                print("please enter a valid option ")
        else:
            contact[name] = {"phone" : phone, "email" : email}
            return
    



def look_up(contact, name):
    if name in contact:
        print(f"Name : {name}")
        print(f"Phone : {contact[name]["phone"]}")
        print(f"Email : {contact[name]["email"]}")
    else:
        print("the name is not present in the contact book, please enter a valid name ")



def delete_contact(contact, name):
    if name in contact:
        del contact[name]
        print(f"the {name}'s contact has been deleted ")
    else:
        print("the name was not found, please enter a valid name")

def list_contact(contact):
    for name, details in contact.items():
        print(f"{name}'s phone number is {details["phone"]} and the email is {details["email"]}")






def main():
    contact = {}
    while True:
        selection = input("""please select one of the following by entering the number
        1. Add/edit a contact
        2. Look up a contact
        3. Delete a contact
        4. List all contacts
        5. Quit
        >>>  """).strip()
        try:
            user_input = int(selection)
            if user_input == 5:
                return            
            elif user_input == 1:
                name = input("please enter the name of the person you wish to add or edit  >  ").lower().strip()
                phone = input("please enter the phone number of the person  >  ")
                email = input("please enter the email of the person  >  ").lower().strip()
                add_or_edit_contact(contact, name, phone, email)
            elif user_input == 2:
                name = input("please enter the name of the person you wish to know about  >  ").lower().strip()
                look_up(contact, name)
            elif user_input == 3:
                name = input("please enter the name of the person whose contact you wish to delete  >  ").lower().strip()
                delete_contact(contact, name)
            elif user_input == 4:
                list_contact(contact)
            else:
                print("please select a valid option")
        except ValueError:
            print("please input a valid number")

        











main()