from dados_globais import lista_turmas
from resources import mensagem

def consultar_alunos_por_turma():
    mensagem("Consultar Alunos por Turma")
    if not lista_turmas:
        print("Nenhuma turma cadastrada.")
        return
    
    # Exibe alunos matriculados em cada turma
    for turma in lista_turmas:
        print(f"Turma: {turma['nome']} - Código: {turma['codigo']}")
        if turma['alunos']:
            for aluno in turma['alunos']:
                print(f"Aluno: {aluno['nome']} - Matrícula: {aluno['matricula']}")
        else:
            print("Nenhum aluno matriculado nesta turma.")