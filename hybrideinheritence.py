class Animal:
    def speak(self):
        return "Animal speaks"

class Bird(Animal):
    def fly(self):
        return "Bird flies"

class Fish(Animal):
    def swim(self):
        return "Fish swims"

class Duck(Bird, Fish):
    def quack(self):
        return "Duck quacks"
d = Duck()
print(d.speak())    
print(d.fly())
print(d.swim())
print(d.quack())

