from resorces import mensagem, opcao_selecionada, gerar_codigo, diciplinas_disponiveis
from random import randint

mensagem("Menu")

alunos = [] # lista para armazenar todos os alunos

def cadastar_aluno():
    print(" 1 - Cadastrar Aluno")
    dados_aluno = {}
    
    nome_aluno = input("Digite o nome do aluno: \n")
    matricula = randint(1000000, 9999999)
    print(f"A matricula gerada é {matricula}") # funciona
    # acho que a matricula tem que ser gerada automaticamente com randint
    
    data_nasc = input("Digite a data de nascimento do aluno: \n")
    sexo = input("Digite o sexo do aluno (M/F): \n").upper()
    while sexo not in ["M","F"]:
        print("Dígito inválido. Digite novamente.")
        sexo = input("Digite o sexo do aluno (M/F): \n").upper()
        
    endereco = input("Digite o endereço do aluno: ")
    telefone = int(input("Digite o telefone do aluno: "))
    
    email = input("Digite o e-mail do aluno: ")
    while "@" not in email:
        print("E-mail inválido. Digite novamente. incluindo @")
        email = input("Digite o e-mail do aluno: ")
        # validar se o email é válido 
    
    # adicionando os dados do aluno em um dicionário
    
    dados_aluno["nome"] = nome_aluno
    dados_aluno["matricula"] = matricula
    dados_aluno["data_nasc"] = data_nasc
    dados_aluno["sexo"] = sexo
    dados_aluno["endereco"] = endereco
    dados_aluno["telefone"] = telefone
    dados_aluno["email"] = email
    
    alunos.append(dados_aluno)
    
    print("Aluno cadastrado com sucesso!")    
    
    # talvez fazer uma maneira de identificar o aluno no sistema 
    
def cadastrar_professor():
    print(" 2 - Cadastrar Professor")
    
    nome_professor = input("Digite o nome do professor: \n")
    gerar_codigo()
    data_nasc = input("Digite a data de nascimento do professor: \n")
    
    sexo = input("Digite o sexo do professor (M/F): \n").upper()
    while sexo not in ["M","F"]:
        print("Dígito. Digite novamente.")
        sexo = input("Digite o sexo do professor (M/F): \n").upper()
    
    endereco = input("Digite o endereço do professor: ")
    telefone = int(input("Digite o telefone do professor: "))
    
    email = input("Digite o e-mail do professor: ")
    while "@" not in email:
        print("E-mail inválido. Digite novamente. incluindo @ no email")
        email = input("Digite o e-mail do professor: ")
    
    diciplinas_disponiveis()
    #opcoes de disciplinas disponiveis
    
    def matematica():
        print("1 - Matemática")
        print("Funcionalidade de cadastro de turma ainda não implementada.")
    def portugues():
        print("2 - Português")
        print("Funcionalidade de cadastro de turma ainda não implementada.")
        
    opcoes = {
        1: "Matemática",
        2: "Português",
    }
    
    disciplina = int(input("Digite a disciplina do professor: \n"))
    
    
    
def cadastrar_disciplina():
    print(" 3 - Cadastrar Disciplina")
    print("Funcionalidade de cadastro de disciplina ainda não implementada.")
    # isso é uma funcao placeholder
    
def cadastrar_turma():
    print(" 4 - Cadastrar Turma")
    print("Funcionalidade de cadastro de turma ainda não implementada.")
    
opcoes = {
    1: cadastar_aluno,
    2: cadastrar_professor,
    3: cadastrar_disciplina,
    4: cadastrar_turma
}

opcao_escolhida = int(input("Digite a opção desejada: "))

if opcao_escolhida in opcoes: 
    # Se opcao_escolhida estiver em opcoes, a condição é verdadeira e o código dentro do if será executado.
    opcoes[opcao_escolhida]()
else:
    print("Opção inválida")



    
    
   # - Crie um sistema escolar que permita cadastrar alunos, professores, disciplinas e turmas.