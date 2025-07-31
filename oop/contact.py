class Contact:
    def __init__(self, name, phone, email):
        self.name = name
        self.phone = phone
        self.email = email

    def show(self):
        print("Name:", self.name)
        print("Phone:", self.phone)
        print("Email:", self.email)

contact1 = Contact("Sara", "0791234567", "sara@example.com")
contact1.show()
