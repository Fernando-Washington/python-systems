from dados_globais import lista_disciplinas
from resources import mensagem

def consultar_professores_por_disciplina():
    mensagem("Consultar Professores por Disciplina")
    if not lista_disciplinas:
        print("Nenhuma disciplina cadastrada.")
        return
    
    for disciplina in lista_disciplinas:
        professor = disciplina.get('professor', 'Nenhum professor alocado')
        print(f"Disciplina: {disciplina['nome']}")
        print(f"Professor: {professor['nome']}")   