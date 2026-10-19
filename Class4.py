#accesing and modifying data
#1. The traditional way: make the data private and use gatters and setters
class user:
    def __init__ (self, username, email, password):
        self.username = username
        self._email = email
        self.password = password
        
    def clean_email(self):
        return self._email.lower().strip()
        
        
user1 = user("Kamera", "Kmr@gmail.com", 57527)
        
print(user1._email)
user1._email = "owkystgwhw"
print(user1.clean_email())



#Getters
class User:
    def __init__(self, email):
        self._email = email

    def __str__(self):
        return self._email
        
user1 = User("henry@gmail.com")

print(user1.get_email())

print(user1)


#Setters

class User:
    def __init__(self, email):
        self._email = email

    def set_email(self, new_email):
        self._email = new_email.strip().lower()
        
user1 = User("henry@gmail.com")

user1.set_email("  NEW@GMAIL.COM  ")

print(user1._email)
