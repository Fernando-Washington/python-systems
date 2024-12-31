from dados_globais import lista_alunos, lista_turmas
from resources import mensagem

def matricular_aluno_em_turma():
    mensagem("Matricular Aluno em turma")
    if not lista_alunos:
        print("Você precisa cadastrar alunos primeiro")
        return
    elif not lista_turmas:
        print("Você precisa cadastrar turmas primeiro")
        return
    
    print("Alunos cadastrados:")
    for i, aluno in enumerate(lista_alunos):
        print(f"{i+1} - {aluno['nome']} Matricula: {aluno['matricula']}")
    aluno_escolhido = int(input("Digite o número do aluno que deseja matricular: ")) - 1
    
    print("Turmas cadastradas:")
    for i, turma in enumerate(lista_turmas):
        print(f"{i+1} - {turma['nome']} Código: {turma['codigo']}")
    turma_escolhida = int(input("Digite o número da turma que deseja matricular: ")) - 1
    
    lista_alunos[turma_escolhida]['alunos'].append(lista_alunos[aluno_escolhido])
    print(f"Aluno {lista_alunos[aluno_escolhido]['nome']} matriculado na turma {lista_turmas[turma_escolhida]['nome']} com sucesso!")
    
    # alunos e turmas serão listas globais