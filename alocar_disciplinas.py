from dados_globais import lista_disciplinas, lista_turmas
from resources import mensagem

def alocar_disciplina_em_turma():
    """função responsável por alocar disciplina em turma e armazenar dados a lista_turmas
    """
    mensagem("Alocar Disciplina em Turma")

    if not lista_disciplinas:
        print("Nenhuma disciplina cadastrada. Cadastre uma disciplina primeiro.")
        return
    if not lista_turmas:
        print("Nenhuma turma cadastrada. Cadastre uma turma primeiro.")
        return

    print("Disciplinas disponíveis:")
    disciplinas_validas = [disciplina for disciplina in lista_disciplinas if disciplina.get('nome')]
    if not disciplinas_validas:
        print("Nenhuma disciplina válida cadastrada.")
        return
    
    for i, disciplina in enumerate(disciplinas_validas):
        print(f"{i+1} - {disciplina['nome']}")
        
    escolha_disciplina = input("Selecione o número da disciplina: ")
    if not escolha_disciplina.isdigit() or int(escolha_disciplina)-1 not in range(len(disciplinas_validas)):
        print("Entrada inválida.")
        return
    disciplina = disciplinas_validas[int(escolha_disciplina) - 1]

    print("Turmas disponíveis:")
    turmas_validas = [turma for turma in lista_turmas if turma.get('nome')]
    if not turmas_validas:
        print("Nenhuma disciplina válida cadastrada.")
        return
    
    for i, turma in enumerate(turmas_validas):
        print(f"{i+1} - {turma['nome']}")
        
    escolha_turma = input("Selecione o número da turma: ")
    if not escolha_turma.isdigit() or int(escolha_turma) - 1 not in range(len(lista_turmas)):
        print("Entrada inválida.")
        return

    turma = lista_turmas[int(escolha_turma) - 1]
    turma.setdefault('disciplinas', []).append(disciplina)
    print(f"Disciplina {disciplina['nome']} alocada na turma {turma['nome']} com sucesso!")
    
    # ""setdefault" is a Dictionary method which will search for a key in the dictionary if that key is present then it will return the value of that key
    