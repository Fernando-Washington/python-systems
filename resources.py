from random import randint

# exibir mensagem formatada
def mensagem(msg):
    print("-" * 30)
    print(msg.center(30))
    print("-" * 30)

# exibe opcoes do menu principal
def menu_opcoes():
    print("------------------------------")
    print("-  1 - Cadastrar Aluno       -")
    print("-  2 - Cadastrar Professor   -")
    print("-  3 - Cadastrar Disciplina  -")
    print("-  4 - Cadastrar Turma       -")
    print("-  5 - Sair                  -")
    print("------------------------------")

# função para gerar código no formato A1234
def gerar_codigo():
    letra = "A"
    numeros = randint(1000, 9999)
    codigo = f"{letra}{numeros}"
    return codigo


             
        
