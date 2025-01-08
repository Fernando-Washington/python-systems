from dados_globais import lista_disciplinas, lista_professores
from resources import gerar_codigo, mensagem

# cadastro de disciplinas
def cadastrar_disciplina():
    """função responsável por cadastrar disciplina e armazenar dados em lista_disciplinas
    """
    mensagem("Cadastar Disciplina")
    
    nome_disciplina = input("Digite o nome da disciplina: \n")
    codigo = gerar_codigo()
    carga_horaria = int(input("Digite a carga horária da disciplina em horas: \n"))

    # logica para vincular professor a disciplina
    if lista_professores: # se a lista nãoe stiver vazia retornará True
        print("Professores já cadastrados: ")
        for i, item in enumerate(lista_professores): 
            print(f"{i + 1} - {item['nome']}") 
            # exibindo os professores cadastrados para garantir que nomes de disciplinas de forma numerada
            escolha = int(input("Selecione o número do professor responsável pela disciplina \n")) - 1 # -1 pois a lista começa do 0
        if 0 <= escolha < len(lista_professores):    
            professor_selecionado = lista_professores[escolha]["nome"]
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