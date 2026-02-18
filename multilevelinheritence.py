class Animal:
 def speak(self):
    return "Animal speaks"
class Dog(Animal):
 def bark(self):
    return "Dog barks"
class Cat(Animal):
 def meow(self):
     return "Cat meows"
d = Dog()
c = Cat()   
print(d.speak())  # Inherited from Animal
print(d.bark())   # Dog's own method    
print(c.speak())  # Inherited from Animal
print(c.meow())   # Cat's own method