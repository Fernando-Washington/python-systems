from resources import gerar_codigo

diciplinas = []
def cadastrar_disciplina():
    print(" 3 - Cadastrar Disciplina")
    
    nome_disciplina = input("Digite o nome da disciplina: \n")
    codigo = gerar_codigo()
    carga_horaria = int(input("Digite a carga horária da disciplina em horas: \n"))
    nome_professor = input("Digite o nome do professor responsável: \n")
    '''carga_horaria = f"{carga_horaria} horas"'''
    
    dados_diciplina = {}
    
    dados_diciplina["nome"] = nome_disciplina
    dados_diciplina["codigo"] = codigo
    dados_diciplina["carga_horaria"] = carga_horaria
    dados_diciplina["professor"] = nome_professor
    diciplinas.append(dados_diciplina)
    
    print("Disciplina cadastrada com sucesso!")
    print(dados_diciplina) # placeholder
    
    # nome codigo carga hora