from random import randint
alunos = []

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