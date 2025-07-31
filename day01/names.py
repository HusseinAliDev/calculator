name = input("What is your name?")
age = int(input("How old are you?"))
year = 2025 - age
print(f"Your birth year is {year}")



for i in range(1, 6):
    print(f"Number: {i}")

my_list = [5, 10, 15]
total = 0
for num in my_list:
    total += num
print("Sum:", total)


def add(x, y):
    return x + y

print("Sum is:", add(4, 6))
print("Test new branch")
