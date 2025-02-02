from dados_globais import lista_professores
from resources import gerar_codigo, mensagem

professores = []

# cadastro de professores incluindo disciplina associada
def cadastrar_professor():
    """função responsável por cadastrar professor e armazenar dados em lista_professores
    """
    mensagem("Cadastrar Professor")
    
    nome_professor = input("Digite o nome do professor: \n")
    codigo = gerar_codigo()
    data_nasc = input("Digite a data de nascimento do aluno (DD/MM/AAAA): \n")
    
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
    
    # adicionando os dados do professor em um dicionário
    
    dados_professor = {
        "nome": nome_professor,
        "codigo": codigo,
        "nascimento": data_nasc,
        "sexo": sexo,
        "endereco": endereco,
        "telefone": telefone,
        "email": email,
        "disciplinas": []
    }
    
    lista_professores.append(dados_professor)
    print("Professor cadastrado com sucesso!")
