class User:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show(self):
        print(f"Name: {self.name}, Age: {self.age}")

users = []

while True:
    print("\nChoose action:")
    print("1. Add user")
    print("2. Show all users")
    print("3. Delete user by name")
    print("4. Exit")
    print("5. Edit user")


    choice = input("Enter your choice: ")

    if choice == "1":
        name = input("Enter name: ")
        age = int(input("Enter age: "))
        user = User(name, age)
        users.append(user)
        print("User added.")

    elif choice == "2":
        for user in users:
            user.show()

    elif choice == "3":
        name_to_delete = input("Enter name to delete: ")
        users = [user for user in users if user.name != name_to_delete]
        print("User deleted if found.")

    elif choice == "4":
        name_to_update = input("Enter name to delete: ")
        new_name = input("Enter a newname: ")
        new_age = int(input("Enter a newage: "))
        user = User(name, age)
        users.append(user)
        print("User added.")
        
        break
    elif choice == "5":
            print("Goodbye!")
            break
    else:
        print("Invalid choice.")
