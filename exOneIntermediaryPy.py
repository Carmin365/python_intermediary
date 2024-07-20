# Line 1 >> Person class difinition. # Definição da classe person. 
# Line 2 >> In this line, a constructor method, an object and two parameters are defined. The self object is used in methods to access the object´s attibutes. Name is the first parameter of the constructor. Age is the second parameter of the constructor. # Nesta linha é definido um método construtor, um objeto e dois parâmentros. O objeto self é usado em métodos para acessar os atributos do objeto. Nome é o primeiro parâmetro do construtor. Idade é o segundo parâmetro do construtor.
# Line 3 >> Self method being called together with the name variable and assigning a value to it. # Método self sendo chamado juntamente com a variável name e atribuição de valor ao mesmo.
# Line 4 >> Self method being called together with the age variable and assingning a value to it. # Método self sendo chamado juntamente com a variável age e atribuição de valor ao mesmo.
# Line 5 >> Definition of the to_present method and the Self parameter being called. # Definição do método to_present e o parâmentro Self sendo chamado.
# Line 6 >> This line of code is using an f string to shows a formatted messagge in the console. # Esta linha de código está usando uma string f para mostrar uma mensagem formatada no console.
class Person:
    def __init__ (self, name, age):
        self.name = name
        self.age = age
        def to_present(self):
            print(f"Hello, my name is {self.name} and I have {self.age} years.")

            # Line 7 >> Creation of the person1 variable and assigning a value to it. This Person value characterizes the instance of a class. # Criação da variável person1 e atribuição de valor à mesma. Este valor Person caracteriza a instância de uma classe. 
            # Line 8 >> This line calls the to_present method on an object cited by the person1 variable. # Esta linha chama o método to_present em um objeto citado pela variável person1.
            personI = Person("Pietro", 45)
            personI.to_present()
