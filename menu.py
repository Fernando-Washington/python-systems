from resorces import mensagem, opcao_selecionada, gerar_codigo, diciplinas_disponiveis, menu_opcoes
from random import randint

mensagem("Menu")
menu_opcoes()

alunos = [] # lista para armazenar todos os alunos

# variaveis com escopo global podem ter o mesmo nome em diferentes funções

# parte 1

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
    dados_aluno["nascimento"] = data_nasc
    dados_aluno["sexo"] = sexo
    dados_aluno["endereco"] = endereco
    dados_aluno["telefone"] = telefone
    dados_aluno["email"] = email
    
    alunos.append(dados_aluno)
    
    print("Aluno cadastrado com sucesso!")    
    
    # talvez fazer uma maneira de identificar o aluno no sistema 
 
 
# parte 2 --------------------------
    

professores = []
    
def cadastrar_professor():
    print(" 2 - Cadastrar Professor")
    
    nome_professor = input("Digite o nome do professor: \n")
    codigo = gerar_codigo()
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
        
    disciplina_professor = input("Digite o nome da disciplina do professor")   
    
    # adicionando os dados do professor em um dicionário
    
    dados_professor = {}
    
    dados_professor["nome"] = nome_professor
    
    dados_professor["codigo"] = codigo
    dados_professor["nascimento"] = data_nasc
    dados_professor["sexo"] = sexo
    dados_professor["endereco"] = endereco
    dados_professor["telefone"] = telefone
    dados_professor["email"] = email  
    dados_professor["disciplina"] = disciplina_professor
    
    print("Professor cadastrado com sucesso!")
    print(dados_professor)
    
    '''
    diciplinas_disponiveis()
    #opcoes de disciplinas disponiveis
    
    opcoes = {
        1: "Matemática",
        2: "Português",
    }
    
    disciplina = int(input("Digite o número correspondente a disciplina \n"))'''
    
    
diciplinas = []
def cadastrar_disciplina():
    print(" 3 - Cadastrar Disciplina")
    
    nome_disciplina = input("Digite o nome da disciplina: \n")
    codigo = gerar_codigo()
    carga_horaria = int(input("Digite a carga horária da disciplina em horas: \n"))
    nome_professor = input("Digite o nome do professor responsável: \n")
    '''carga_horaria = f"{carga_horaria} horas"'''
    
    dados_diciplina = {}
    
    dados_diciplina["nome"] = nome_disciplina
    dados_diciplina["codigo"] = codigo
    dados_diciplina["carga_horaria"] = carga_horaria
    dados_diciplina["professor"] = nome_professor
    diciplinas.append(dados_diciplina)
    
    print("Disciplina cadastrada com sucesso!")
    print(dados_diciplina) # placeholder
    
    # nome codigo carga horaria professor
turma = []  
    
def cadastrar_turma():
    print(" 4 - Cadastrar Turma")
    
    nome_turma = input("Digite o nome da turma: \n")
    codigo = gerar_codigo()
    nome_disciplina = input("Digite o nome da disciplina: \n")
    
    # queria que essa parte possuisse a opção de escolher a disciplina ja cadastrada e vincular a turma a ela de alguma forma, não só nessa funcao mas nas outras tambem
    
    nome_professor = input("Digite o nome do professor responsável: \n")
    
    dados_turma = {}
    
    dados_turma["nome"] = nome_turma
    dados_turma["codigo"] = codigo
    dados_turma["disciplina"] = nome_disciplina
    dados_turma["professor"] = nome_professor
    
    turma.append(dados_turma)
    
    print("Turma cadastrada com sucesso!")
    print(dados_turma) # placeholder
    
    # nome codigo disciplina professor alunos (lista-matricula)
    
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