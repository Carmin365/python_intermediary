# Line 1 >> This line defines the main function of the code and assigns it the value (data_type). # Esta linha define a função principal do código e lhe atribui o valor(tipo_dado).  
# Line 2 >> This line defines the decorator function and assigns it the value (function). # Esta linha define a função decorator e lhe é atribuído o valor(funcao). 
# Line 3 >> This line defines the decorated_function and the values ​​(*args, **kwargs) are assigned to it. # Esta linha define a funcao_decorada e lhe são atribuídos os valores (*args, **kwargs). 
# Line 4 >> This line characterizes the beginning of the for loop and uses the variable args. # Esta linha caracteriza o inicio do laço for e utiliza a vaiável args.
# Line 5 >> This line features an 'if' conditional structure that uses the isinstance() function to confirm that the 'arg' object is not an instance of the type described in 'data_type'. # Esta linha caracteriza uma estrutura condicional 'if' que usa a função isinstance() para confirmar se o objeto 'arg' não é uma instância do tipo descrito em 'tipo_dado'. 
# Line 6 >> This line indicates an exception from the 'TypeError' pattern with an edited warning, showing that the argument provided is not of the expected pattern. # Esta linha indica uma exceção do padrão 'TypeError' com um aviso editado, mostrando que o argumento disponibilizado não é do padrão esperado. 

def autenticar_acesso_decorador(tipo_dado):
    def decorator(funcao):
        def funcao_decorada(*args, **kwargs):
            for arg in args:
                if not isinstance(arg, tipo_dado):
                    raise TypeError(f"Argumento '{arg}' deve ser do tipo {tipo_dado}.")
               
                # Line 7 >> In this line the result variable is declared and two values ​​are assigned to it. 'function' is the name of the function being requested. 'args' and 'kwargs' are two arguments used to unpack lists, tuples and dictionaries. # Nesta linha a variável resultado é declarada e lhe é atribuida dois valores. 'funcao' é o nome da função que está sendo solicitada. 'args' e 'kwargs' são dois argumentos utilizados para desempacotar listas, tuplas e dicionários. 
                # Line 8 >> In this line 'return' returns a value, this value is the value contained in the result variable. # Nesta linha 'return' devolve um valor, este valor é o valor contido na variável resultado. 
                # Line 9 >> In this line 'return' is returning a value and this value is the 'decorator_function' that was defined in line 3 of the code. # Nesta linha 'return' está devolvendo um valor e este valor é a 'funcao_decoradora' que foi definida na linha 3 do código.
                # Line 10 >> In this line 'return' is returning a value and this value is the content of the decorator variable that was defined in line two of the code. # Nesta linha 'return' está devolvendo um valor e este valor é o conteúdo da variável decorator que foi definida na linha dois do código.
                resultado = funcao(*args, **kwargs)
                return resultado 
            return funcao_decorada
        return decorator

    # Line 11 >>
    # Line 12 >>
    # Line 13 >>
    # Line 14 >>
    # Line 15 >>
    @autenticar_acesso_decorador(str)
    def formatar_nome(nome):
        return nome.title()
    nome_formatado = formatar_nome("ana dos santos")
    print(nome_formatado)

    try:
        formatar_nome(123)
    except TypeError as e:
        print(e)
