from dados_globais import lista_turmas
from resources import mensagem

def consultar_disciplinas_por_turma():
    """função responsável por exibir as disciplinas de cada turma
    """
    mensagem("Consultar Disciplinas por Turma")
    if not lista_turmas:
        print("Nenhuma turma cadastrada.")
        return
    
    for turma in lista_turmas:
        print(f"Turma: {turma.get('nome', '(nome ausente)')}")
        disciplinas = turma.get('disciplinas', [])  # Garante que disciplinas seja uma lista
        if disciplinas:
            for disciplina in disciplinas:
                print(f" - {disciplina['nome']} Código: {disciplina['codigo']}")
        else:
            print("Nenhuma disciplina alocada.")

# o .get busca o valor associado a uma chave específica em um dicionário.