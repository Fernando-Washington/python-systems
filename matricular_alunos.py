from dados_globais import lista_alunos, lista_turmas
from resources import mensagem

def matricular_aluno_em_turma():
    mensagem("Matricular Aluno em turma")
    
    # vefica se há alunos e turmas cadastrados
    if not lista_alunos:
        print("Você precisa cadastrar alunos primeiro")
        return
    elif not lista_turmas:
        print("Você precisa cadastrar turmas primeiro")
        return
    
    # exibe alunos e turmas cadastrados
    print("Alunos cadastrados:")
    for i, aluno in enumerate(lista_alunos):
        print(f"{i+1} - {aluno['nome']} Matricula: {aluno['matricula']}")
    
    # solicita ao usuário que escolha um aluno
    aluno_escolhido = int(input("Digite o número do aluno que deseja matricular: ")) - 1
    
    # valida a escolha do aluno
    if aluno_escolhido < 0 or aluno_escolhido >= len(lista_alunos):
        print("Opção inválida.")
        return
    
    # exibe turmas cadastradas
    print("Turmas cadastradas:")
    for i, turma in enumerate(lista_turmas):
        print(f"{i+1} - {turma['nome']} Código: {turma['codigo']}")
        
    # solicita ao usuário que escolha uma turma
    turma_escolhida = int(input("Digite o número da turma que deseja matricular: ")) - 1
    
    # valida a escolha da turma
    if turma_escolhida < 0 or turma_escolhida >= len(lista_turmas):
        print("Opção inválida.")
        return
    
    # verifica se a chave 'alunos' existe na turma escolhida
    if 'alunos' not in lista_turmas[turma_escolhida]:
        lista_turmas[turma_escolhida]['alunos'] = []
    
    # adicionando o aluno a turma escolhida
    lista_turmas[turma_escolhida]['alunos'].append(lista_alunos[aluno_escolhido])
    
    # exibe mensagem de sucesso
    print(f"Aluno {lista_alunos[aluno_escolhido]['nome']} matriculado na turma {lista_turmas[turma_escolhida]['nome']} com sucesso!")
    
    # alunos e turmas serão listas globais