class ContactBook:
    def add_num(self):
        with open("C:/Users/Gaurav/OneDrive/Desktop/contact.txt", 'a') as contact:
            name = input("Name: ")
            phone = input("Phone: ")
            contact.write(f"{name} - {phone}\n")
    
    def view_contact(self):
        with open("C:/Users/Gaurav/OneDrive/Desktop/contact.txt", 'r') as file:
            file_content = file.read()
            print(file_content)
    
    def search_contact(self):
        search_str = input("Enter the content to search: ")
        with open("C:/Users/Gaurav/OneDrive/Desktop/contact.txt", 'r') as file:
            lines = file.readlines()
        found = False
        for line in lines:
            if search_str in line:
                print(f"'{search_str}' found in line: {line.strip()}")
                found = True
                break
        if not found:
            print(f"'{search_str}' not found")

    def update(self):
        index_to_update = int(input("Enter the line number to update: "))
        new_detail = input("Enter the new content for the line: ")
        with open("C:/Users/Gaurav/OneDrive/Desktop/contact.txt", 'r') as file:
            lines = file.readlines()
        if 1 <= index_to_update <= len(lines):
            lines[index_to_update - 1] = new_detail + '\n'
            with open("C:/Users/Gaurav/OneDrive/Desktop/contact.txt", 'w') as file:
                file.writelines(lines)
            print(f"Line {index_to_update} updated successfully.")
        else:
            print(f"Line number {index_to_update} is out of range.")
    
    def contact_delete(self):
        contact_to_delete = input("Enter the content to delete: ")
        with open("C:/Users/Gaurav/OneDrive/Desktop/contact.txt", 'r') as file:
            lines = file.readlines()

        updated_lines = [line for line in lines if contact_to_delete not in line]

        with open("C:/Users/Gaurav/OneDrive/Desktop/contact.txt", 'w') as file:
            file.writelines(updated_lines)
        print(f"Content '{contact_to_delete}' deleted successfully.")

class Main:
    new_cont = ContactBook()
    print("1. add_num")
    print("2. view_contact")
    print("3. search_contact")
    print("4. update")
    print("5. contact_delete")
    print("6.exit")
    choice = int(input("Please choose any option: "))

    if choice == 1:
        new_num = input("Do you want to add a number (y/n)? ").lower()
        while new_num == 'y':
            new_cont.add_num()
            new_num = input("Do you want to add a number (y/n)? ").lower()
            if new_num=='n':
                choice = int(input("Please choose any option: "))
                continue
            
    if choice == 2:
        new_cont.view_contact()
        choice = int(input("Please choose any option: "))
    if choice == 3:
        new_cont.search_contact()
        choice = int(input("Please choose any option: "))
        
    if choice == 4:
        new_cont.update()
        choice = int(input("Please choose any option: "))
        
    if choice == 5:
        new_cont.contact_delete()
        choice = int(input("Please choose any option: "))
    if choice ==6:
        print("contact_book is closing")
        
