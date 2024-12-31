from dados_globais import lista_alunos
from random import randint
from resources import mensagem


# funcao para cadastrar alunos
def cadastar_aluno():
    mensagem("Cadastrar Aluno")
    dados_aluno = {}
    
    nome_aluno = input("Digite o nome do aluno: \n")
    matricula = randint(1000000, 9999999) # matricula aleatoria
    print(f"A matricula gerada é {matricula}") 
    
    data_nasc = input("Digite a data de nascimento do aluno (DD/MM/AAAA): \n")
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
    
    # adicionando os dados do aluno em um dicionário
    
    dados_aluno["nome"] = nome_aluno
    dados_aluno["matricula"] = matricula
    dados_aluno["nascimento"] = data_nasc
    dados_aluno["sexo"] = sexo
    dados_aluno["endereco"] = endereco
    dados_aluno["telefone"] = telefone
    dados_aluno["email"] = email
    
    lista_alunos.append({"nome": nome_aluno, "matricula": matricula})
    print(f"Aluno {dados_aluno['nome']} cadastrado com sucesso!")   