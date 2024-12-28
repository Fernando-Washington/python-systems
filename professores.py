from resources import gerar_codigo

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
        
    disciplina_professor = input("Digite o nome da disciplina do professor: ")   
    
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