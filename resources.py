from random import randint

# exibir mensagem formatada
def mensagem(msg):
    """funcao que exibe mensagem formatada

    Args:
        msg (str): retorna mensagem formatada
    """
    print("-" * 46)
    print(msg.center(46))
    print("-" * 46)

# exibe opcoes do menu principal
def menu_opcoes():
    """funcao que exibe as opcoes do menu principal
    """
    print("----------------------------------------------")
    print("-  1  - Cadastrar Aluno                      -")
    print("-  2  - Cadastrar Professor                  -")
    print("-  3  - Cadastrar Disciplina                 -")
    print("-  4  - Cadastrar Turma                      -")
    print("-  5  - Matricular Aluno em Turma            -")
    print("-  6  - Alocar Professor em Disciplina       -")
    print("-  7  - Alocar Disciplina em Turma           -")
    print("-  8  - Consultar Professores por Disciplina -")
    print("-  9  - Consultar Alunos por Turma           -")
    print("-  10 - Consultar Disciplinas por Turma      -")
    print("-  11 - Sair                                 -")
    print("----------------------------------------------")

# função para gerar código no formato A1234
def gerar_codigo():
    """função que gera um código no formato A0000

    Returns:
        str: retorna o valor do código
    """
    letra = "A"
    numeros = randint(1000, 9999)
    codigo = f"{letra}{numeros}"
    return codigo


             
        
