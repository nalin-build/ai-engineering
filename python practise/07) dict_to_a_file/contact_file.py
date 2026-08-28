def main():
    contacts = {}
    try:
        with open("contact.txt", "r") as file:
            for line in file:
                parts = line.split(",")
                name = parts[0].strip()
                phone = parts[1].strip()
                contacts[name] = phone
    except FileNotFoundError:
        pass

    while True:
        name = input("what is the name of the person or type done to exit:  ").lower().strip()
        if name == "done":
            break
        while True:
            phone = input("what is the phone number of the person: ")
            try:
                phone = int(phone)
                break
            except ValueError:
                print("please input a vaid number ")
        if name in contacts:
            choice = input("the name already exists in the dictionary are you sure you want to make the changes press y/n: ").lower()
            if choice == "y":
                contacts[name] = phone
                continue
            else:
                continue
        else:
            contacts[name] = phone

    with open("contact.txt", "w") as file:
        for name, phone in contacts.items():
            file.write(f"{name}, {phone}\n")





main()
