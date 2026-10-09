class user:
    def __init__ (self, username, email, password):
        self.username = username
        self.email = email
        self.password = password
        
    def say_hello(self, user):
        print(f" Message from {user.username}: Hello, {self.username} this is {user.username}")


user1 = user("Akhakal", "Akh@gmail.com", 57527)
user2 = user("Jerrmy", "Jeremy@gmail.com", 65294)


print(user1.say_hello(user2))