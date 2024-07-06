class Person:
    def __init__ (self, name, age):
        self.name = name
        self.age = age
        def to_present(self):
            print(f"Hello, my name is {self.nome} and I have {self.idade} years.")
            
            person1 = Person("Pietro", 45)
            person1.to_present()