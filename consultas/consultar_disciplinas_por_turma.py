from dados_globais import lista_turmas
from resources import mensagem

def consultar_disciplinas_por_turma():
    mensagem("Consultar Disciplinas por Turma")
    if not lista_turmas:
        print("Nenhuma turma cadastrada.")
        return
    
    for turma in lista_turmas:
        print(f"Turma: {turma['nome']}")
        if turma['disciplinas']:
            for disciplina in turma['disciplinas']:
                print(f" - {disciplina['nome']} (Código: {disciplina['codigo']})")
        else:
            print("Nenhuma disciplina alocada.")