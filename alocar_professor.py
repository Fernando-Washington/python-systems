from dados_globais import lista_disciplinas, lista_professores
from resources import mensagem

def alocar_professor_em_disciplina():
    mensagem("Alocação de professor em disciplina")
    if not professor: # melhor trocar o nome da variavel por disciplina?
        print("Você precisa cadastrar professores primeiro")
    elif not lista_professores:
        print("Você precisa cadastrar disciplinas primeiro")
        return
    
    print("Professores cadastrados:")
    for i, professor in enumerate(lista_professores):
        print(f"{i+1} - {professor['nome']} Matricula: {professor['matricula']}")
    professor_escolhido = int(input("Digite o número do professor que deseja alocar: ")) - 1

    print("Disciplinas cadastradas:")
    
    print("Disciplinas cadastradas:")
    for i, disciplina in enumerate(lista_disciplinas):
        print(f"{i+1} - {disciplina['nome']} Código: {disciplina['codigo']}")
    disciplina_escolhida = int(input("Digite o número da disciplina que deseja alocar: ")) - 1
    
    disciplina_escolhida['professor'] = lista_professores[professor_escolhido]
    professor_escolhido['disciplinas'].append(disciplina_escolhida)
    print(f"Professor {lista_professores[professor_escolhido]['nome']} alocado na disciplina {disciplina_escolhida['nome']} com sucesso!")
    
    