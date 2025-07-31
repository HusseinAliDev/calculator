class User:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        print("Hello, my name is", self.name)

user1 = User("Ali", 25)
user1.greet()
