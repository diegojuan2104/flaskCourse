class Person: 
    def __init__(self, name, age):
        self.name = name
        self.age = age 

    def __str__(self):
        return f"Person: {self.name}, {self.age} old"

    def __rep
bob = Person("Pepe",33)

print(bob)