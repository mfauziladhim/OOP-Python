class animal:
    def cat(self):
        print("Meow")
        
    def dog(self):
        print("Whoof whoof")
        
animal1 = animal()
animal1.cat()


animal2 = animal()
animal2.dog()

class animal:
    def __init__ (self, name, hobby):
        self.name = name
        self.hobby = hobby
        
    def animal1():
        print(f"The name of animal is {animal1.name} and the hobby is {animal1.hobby}")
    
animal1 = animal("Bartolomeus", "Ball")
print(animal1.name)
print(animal1.hobby)

animal2 = animal("Justin", "Games")
animal2.name
animal2.hobby
