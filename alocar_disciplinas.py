from dados_globais import lista_disciplinas, lista_turmas
from resources import mensagem

def alocar_disciplina_em_turma():
    mensagem("Alocar Disciplina em Turma")

    if not lista_disciplinas:
        print("Nenhuma disciplina cadastrada. Cadastre uma disciplina primeiro.")
        return
    if not lista_turmas:
        print("Nenhuma turma cadastrada. Cadastre uma turma primeiro.")
        return

    print("Disciplinas disponíveis:")
    for i, disciplina in enumerate(lista_disciplinas):
        print(f"{i+1} - {disciplina['nome']}")

    try:
        escolha_disciplina = int(input("Selecione o número da disciplina: ")) - 1
    except ValueError:
        print("Entrada inválida.")
        return

    if 0 <= escolha_disciplina < len(lista_disciplinas):
        disciplina = lista_disciplinas[escolha_disciplina]
    else:
        print("Seleção inválida.")
        return

    print("Turmas disponíveis:")
    for i, turma in enumerate(lista_turmas):
        print(f"{i+1} - {turma['nome']}")

    try:
        escolha_turma = int(input("Selecione o número da turma: ")) - 1
    except ValueError:
        print("Entrada inválida.")
        return

    if 0 <= escolha_turma < len(lista_turmas):
        turma = lista_turmas[escolha_turma]
        turma["disciplinas"].append(disciplina)
        print(f"Disciplina {disciplina['nome']} alocada à turma {turma['nome']} com sucesso!")
    else:
        print("Seleção inválida.")
