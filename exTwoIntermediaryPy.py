# Line 1 >> This line characterizes the beginning of the try block. # Esta linha cacacteriza o começo do bloco try.
# Line 2 >> In this line the variable number is declared and a value is assigned to it. This value is of type int and characterizes a request to the user. # Nesta linha a variável number é declarada e um valor à ela é atribuído. Este valor é do tipo int e caracteriza uma requisição ao usuário. 
# Line 3 >> This line validates if the value of number is less than or equal to zero (<=) # Esta linha valida se o valor de number é menor ou igual à zero(<=).
# Line 4 >> As number is less than or equal to zero, this line projects a ValueError exception with a message. # Como number é menor ou igual a zero, esta linha projeta uma exceção do tipo ValueError com uma mensagem. 
# Line 5 >> This line shows a message on the screen, but will only be executed if the number is positive and no error occurs. f-string (formatted string f) is used to insert the value of number**2(squared number) into the message. # Esta linha mostra uma mensagem na tela, mas somente será executada se o número for positivo e nenhum erro ocorrer. f-string (cadeia formatada f) é utilizada para inserir o valor de number**2(numero ao quadrado) na mensagem. 
# Line 6 >> This except block is performed if an exception of type ValueError is thrown within the try block. The as keyword grants the exception to the variable e. # Este bloco except é realizado se uma exceção do tipo ValueError for projetada dentro do bloco try. A palavra-chave as concede a exceção à variável e.     
# Line 7 >> The line print(f"Error:{e}") shows a custom error message, including the projected exception message(e). # A linha print(f"Error:{e}") mostra uma mensagem de erro personalizada, incluindo a mensagem da exceção projetada(e). 
# Line 8 >> This "except" block is a common exception conquer block. It will take effect if any exception (other than ValueError) happens inside the "try" block. # Este bloco "except" é um bloco comum de coquista de exceção. Ele será efetivado se qualquer exceção (além de ValueError) acontecer dentro do bloco "try".
# Line 9 >> As per the previous block, the exception is caught in variable e and a generic error message is shown. # Conforme o bloco anterior, a exceção é conquistada na variável e e uma mensagem de erro genérica é mostrada.
try:
    number = int(input("Enter a number"))
    if number <= 0:
        raise ValueError("The number must be positive")
    print(f"the square of the number is: {number ** 2}")
except ValueError as e:
    print(f"Error: {e}")
except Exception as e:
    print(f"Unexpected error: {e}")
