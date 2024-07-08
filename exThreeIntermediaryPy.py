def autenticar_acesso_decorador(tipo_dado):
    def decorator(funcao):
        def funcao_decorada(*args, **kwargs):
            for arg in args:
                if not isinstance(arg, tipo_dado):
                    raise TypeError(f"Argumento '{arg}' deve ser do tipo {tipo_dado}.")
                
                resultado = funcao(*args, **kwargs)
                return resultado 
            return funcao_decorada
        return decorator
    
    @autenticar_acesso_decorador(srt)
    def formatar_nome(nome):
        return nome.title()
    nome_formatado = formatar_nome("ana dos santos")
    print(nome_formatado)

    try:
        formatar_nome(123)
    except TypeError as e:
        print(e)
