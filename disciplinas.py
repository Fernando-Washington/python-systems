from dados_globais import lista_disciplinas
from resources import gerar_codigo, mensagem
from professores import professores

# cadastro de disciplinas
def cadastrar_disciplina():
    mensagem("Cadastar Disciplina")
    
    nome_disciplina = input("Digite o nome da disciplina: \n")
    codigo = gerar_codigo()
    carga_horaria = int(input("Digite a carga horária da disciplina em horas: \n"))

    # logica para vincular professor a disciplina
    if professores: # se a lista nãoe stiver vazia retornará True
        print("Professores já cadastrados: ")
        for i, item in enumerate(professores): 
            print(f"{i + 1} - {item['nome']}") 
            # exibindo os professores cadastrados para garantir que nomes de disciplinas de forma numerada
            escolha = int(input("Selecione o número do professor respomsável pela disciplina \n")) - 1 # -1 pois a lista começa do 0
        if 0 <= escolha < len(professores):    
            professor_selecionado = professores[escolha]["nome"]
        else:
            print("Seleção inválida.")
            return
    else: 
        print("Nenhum professor cadastrado. Cadastre um professor antes de continuar")
        return
    
    '''carga_horaria = f"{carga_horaria} horas"'''
    
    dados_disciplina = {
        "nome": nome_disciplina,
        "codigo": codigo,
        "carga_horaria": carga_horaria,
        "professor": professor_selecionado
    }
    
    lista_disciplinas.append(dados_disciplina)
    print("Disciplina cadastrada com sucesso!")