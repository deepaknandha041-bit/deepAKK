class Phone:
    def call(self):
        return "Can make calls"

class Camera:
    def take_photo(self):
        return "Can take photos"

class SmartPhone(Phone, Camera):
    def browse(self):
        return "Can browse the internet"

# Create object
s = SmartPhone()

print(s.call())
print(s.take_photo())
print(s.browse())
