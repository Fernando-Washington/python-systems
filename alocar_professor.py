from dados_globais import lista_disciplinas, lista_professores
from resources import mensagem

def alocar_professor_em_disciplina():
    """função responsável por alocar um professor em uma disciplina e armazenar dados a lista_professores
    """
    mensagem("Alocação de professor em disciplina")
    # verifica se existem professores cadastrados
    if not lista_professores: # melhor trocar o nome da variavel por disciplina?
        print("Você precisa cadastrar professores primeiro")
        return
    
    # verifica se existem disciplinas cadastradas
    if not lista_disciplinas:
        print("Você precisa cadastrar disciplinas primeiro")
        return
    
    # Lista os professores cadastrados
    print("Professores cadastrados:")
    for i, professor in enumerate(lista_professores):
        print(f"{i+1} - {professor['nome']} Código: {professor['codigo']}")
    professor_escolhido = int(input("Digite o número do professor que deseja alocar: ")) - 1
    
    # validadação do professor escolhido
    if professor_escolhido not in range(len(lista_professores)):
        print("Opção inválida.")
        return

    # Lista as disciplinas cadastradas 
    print("Disciplinas cadastradas:")
    for i, disciplina in enumerate(lista_disciplinas):
        print(f"{i+1} - {disciplina['nome']} Código: {disciplina['codigo']}")
    disciplina_escolhida = int(input("Digite o número da disciplina que deseja alocar: ")) - 1
    
    if disciplina_escolhida not in range(len(lista_disciplinas)):
        print("Opção inválida.")
        return  
    
    # Aloca o professor na disciplina escolhida
    lista_disciplinas[disciplina_escolhida]['professor'] = lista_professores[professor_escolhido]
    lista_professores[professor_escolhido]['disciplinas'].append(lista_disciplinas[disciplina_escolhida])
    
    # Adiciona a disciplina ao professor 
    print(f"Professor {lista_professores[professor_escolhido]['nome']} alocado na disciplina {lista_disciplinas[disciplina_escolhida]['nome']} com sucesso!")
    
    