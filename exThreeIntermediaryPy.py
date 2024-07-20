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

    # Line 11 >> In this line the symbol '@' is used to introduce a decorator to a function, the function here is 'autenticar_acesso_decorador' and (str) is the type of information that the function will return. # Nesta linha o símbolo '@' serve para introduzir um decorador a uma função, a função aqui é 'autenticar_acesso_decorador' e (str) é o tipo de informação que a função vai retornar.
    # Line 12 >> In this line the function 'formatar_nome' is defined and the value 'name' in parentheses characterizes the function parameter being passed. # Nesta linha a função 'formatar_nome é definida e o valor 'nome' entre parênteses caracteriza o parâmetro da função que está sendo passado. 
    # Line 13 >> This characterizes the result of the previous operation and .title() is a method of the str class that modifies the string to the title "model", where the first letter of each word will be capitalized and the rest lowercase. # Esta caracteriza o resultado da operação anterior e .title() é um método da classe str que modifica a string para o "modelo" título, onde a primeira letra de cada palavra será maiúscula e as demais minúsculas.
    # Line 14 >> In this line formatado_nome is a variable and the value 'formatar_nome' is being assigned to it. The content inside the parentheses characterizes the argument being passed by the function, as well as the value that the function will trigger. # Nesta linha nome_formatado é uma variável e se lhe está sendo atribuído o valor 'formatar_nome'. O conteúdo dentro dos parênteses caracteriza o argumento que está sendo passado pelo função, bem como o valor que a função irá acionar. 
    # Line 15 >> In this line print(format_name) indicates that the value inside the parentheses will be shown on the screen (console). This value is the content of the 'formatted_name' variable that was declared in the previous line. # Nesta linha print(nome_formatado) indica que o valor dentro dos parênteses será mostrado na tela(console). Este valor é o conteúdo da variável 'nome_formatado' que foi declarada na linha anterior.
    @autenticar_acesso_decorador(str)
    def formatar_nome(nome): 
        return nome.title()
    nome_formatado = formatar_nome("ana dos santos")
    print(nome_formatado)

    # Line 16 >> This starts a 'try:' block that is used to capture and handle possible exceptions (errors). # Esta inicia um bloco 'try:' que é utilizado para confiscar e tratar passíveis exceções(erros).
    # Line 17 >> This line indicates the function that was defined in line 12 of the code and the content inside the parentheses means the argument being sent by the function. # Esta linha indica a função que foi definida na linha 12 do código e o conteúdo dentro dos parênteses significa o argumento que está sendo enviado pela função. 
    # Line 18 >>
    # Line 19 >>
    try:
        formatar_nome(123)
    except TypeError as e:
        print(e)
