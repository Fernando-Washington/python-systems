from dados_globais import lista_alunos, lista_turmas
from resources import mensagem

def matricular_aluno_em_turma():
    """
    função que matricula alunos em turmas e armazena os dados na lista_turmas
    """
    mensagem("Matricular Aluno em turma")
    
    # vefica se há alunos e turmas cadastrados
    if not lista_alunos:
        print("Você precisa cadastrar alunos primeiro")
        return
    
    turmas_validas = [turma for turma in lista_turmas if turma.get('codigo')]
    if not turmas_validas:
        print("Você precisa cadastrar turmas primeiro")
        return
    
    # exibe alunos e turmas cadastrados
    print("Alunos cadastrados:")
    for i, aluno in enumerate(lista_alunos):
        print(f"{i+1} - {aluno['nome']} Matricula: {aluno['matricula']}")
    
    # solicita ao usuário que escolha um aluno
    aluno_escolhido = input("Digite o número do aluno que deseja matricular: ")
    if not aluno_escolhido.isdigit() or int(aluno_escolhido) - 1 not in range(len(lista_alunos)):
        print("Opção inválida.")
        return
    aluno_escolhido = int(aluno_escolhido) - 1
    
    # exibe turmas cadastradas
    print("Turmas cadastradas:")
    for i, turma in enumerate(turmas_validas):
        print(f"{i+1} - {turma['nome']} Código: {turma['codigo']}")
        
    # solicita ao usuário que escolha uma turma
    turma_escolhida = input("Digite o número da turma que deseja matricular: ") 
    if not turma_escolhida.isdigit() or int(turma_escolhida) - 1 not in range(len(turmas_validas)):
        print("Opção inválida.")
        return
    turma_escolhida = int(turma_escolhida) - 1

    # adicionando o aluno a turma escolhida
    turmas_validas[turma_escolhida].setdefault('alunos', []).append(lista_alunos[aluno_escolhido])
    
    # exibe mensagem de sucesso
    print(f"Aluno {lista_alunos[aluno_escolhido]['nome']} matriculado na turma{lista_turmas[turma_escolhida]['nome']} com sucesso!")
    
    # alunos e turmas serão listas globais