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
               
                # Line 7 >> 
                # Line 8 >>
                # Line 9 >>
                # Line 10 >>
                resultado = funcao(*args, **kwargs)
                return resultado 
            return funcao_decorada
        return decorator
    
    @autenticar_acesso_decorador(str)
    def formatar_nome(nome):
        return nome.title()
    nome_formatado = formatar_nome("ana dos santos")
    print(nome_formatado)

    try:
        formatar_nome(123)
    except TypeError as e:
        print(e)
