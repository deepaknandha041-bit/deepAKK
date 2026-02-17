class school:
    def __init__(self):
        self.name = input("Enter your name: ")
        self.SSLC_Mark = int(input("Enter your 10th Mark: "))
        self.stream = None   # Initialize stream

    def group(self):
        if self.SSLC_Mark > 400:
            print("You are going to Group1")
            self.stream = "Group1"
        elif 300 < self.SSLC_Mark <= 400:
            print("You are going to Group2")
            self.stream = "Group2"
        elif 200 <= self.SSLC_Mark <= 300:
            print("You are going to Group3")
            self.stream = "Group3"
        else:
            print("Marks too low. Not eligible for any group.")
            self.stream = "Not Eligible"

        self.HSC_Mark = int(input("Enter your 12th Mark: "))


class college(school):
    def courses(self):
        if self.stream == "Group1" and self.HSC_Mark > 500:
            print("You are eligible to become a Doctor or Engineer")
        elif self.stream == "Group2" and self.HSC_Mark > 450:
            print("You are eligible to become a Nurse or Teacher")
        elif self.stream == "Group3" and self.HSC_Mark > 350:
            print("You are eligible to become a Manager or Accountant")
        else:
            print("Not eligible for the selected course.")

    def display(self):
        print("\n-- Student Details --")
        print("Name:", self.name)
        print("SSLC Mark:", self.SSLC_Mark)
        print("HSC Mark:", self.HSC_Mark)
        print("Stream:", self.stream)


# Create object
c = college()
c.group()
c.courses()   # You forgot this
c.display()
