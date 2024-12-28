from random import randint

# funções

# função para exibir mensagem
def mensagem(msg):
    print("-" * 30)
    print(msg.center(30))
    print("-" * 30)

def menu_opcoes():
    print("------------------------------")
    print("-  1 - Cadastrar Aluno       -")
    print("-  2 - Cadastrar Professor   -")
    print("-  3 - Cadastrar Disciplina  -")
    print("-  4 - Cadastrar Turma       -")
    print("-  5 - Sair                  -")
    print("------------------------------")
    
# função para selecionar opção
def opcao_selecionada(msg):
    print("Opção selecionada: \n" + msg)

# função para gerar código
def gerar_codigo():
    letra = "A"
    numeros = randint(1000, 9999)
    codigo = f"{letra}{numeros}"
    return codigo

# função para exibir diciplinas disponíveis
def diciplinas_disponiveis():
    print("Disciplinas disponíveis:")
    print("1 - Matemática")
    print("2 - Português")
    
    """print("2 - Português")
    print("3 - História")
    print("4 - Geografia")
    print("5 - Física")
    print("6 - Biologia")
    print("7 - Química")
    print("8 - Filosofia")
    print("9 - Sociologia")
    print("10 - Inglês")"""
    
          

def voltar():
    print("Caso queira voltar a opção anterior digite voltar a qualquer momento")#?? verificar se isso é necessário
    

             
        
