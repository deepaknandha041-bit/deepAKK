class student:
    def __init__(self):
        self.name = input("Enter name: ")
        self.age = int(input("Enter age: "))
    def display(self):
        print(f"Name: {self.name}, Age: {self.age}")
s1 = student()
s1.display()