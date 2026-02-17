class school:
    def __init__(self):
        self.name=input("Enter your name: ")
        self.SSLC_Mark=int(input("Enter your 10th Mark: "))
    def group(self):
        if(self.SSLC_Mark>400):
            print("You are going to Group1")
            self.stream="Group1"
        elif(self.SSLC_Mark>300 and self.SSLC_Mark<=400 ):
            print("You are going to Group2")
            self.stream="Group2"
        elif(self.SSLC_Mark>=200 and self.SSLC_Mark<=300 ):
            print("You are going to Group3")
            self.stream="Group3"
        self.HSC_Mark=int(input("Enter your 12th Mark: "))
class college(school):
    def courses(self):
        if(self.stream=="Group1" and self.HSC_Mark >500):
            print("You are eligible to become an Doctor or Engineer")
        elif(self.stream=="Group2" and self.HSC_Mark >500):
            print("You are eligible to become an Nursing or Teacher")
        elif(self.stream=="Group3" and self.HSC_Mark >500):
            print("You are eligible to become an Manager or Accountant") 
    def display(self):
        print("--student details--")
        print("Name:",self.name)
        print("SSLC Mark:",self.SSLC_Mark)
        print("HSC Mark:",self.HSC_Mark)
        print("Stream:",self.stream)
c=college()
c.group()    
c.display()