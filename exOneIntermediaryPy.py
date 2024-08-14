class Person:
    def __init__ (self, name, age):
        self.name = name
        self.age = age
        def to_present(self):
            print(f"Hello, my name is {self.name} and I have {self.age} years.")

            personI = Person("Pietro", 45)
            personI.to_present()
