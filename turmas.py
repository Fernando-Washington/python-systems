from resources import gerar_codigo
from disciplinas import diciplinas
    # nome codigo carga horaria professor
turmas = []  

# cadastro de turmas
def cadastrar_turma():
    print(" 4 - Cadastrar Turma")
    
    nome_turma = input("Digite o nome da turma: \n")
    codigo = gerar_codigo()
    
    if diciplinas:
        print("Disciplinas disponíveis:")
        for i, item in enumerate(diciplinas):
            print(f"{i + 1} - {item['nome']}")
        escolha = int(input("Selecione o número da disciplina")) - 1
        if 0 <= escolha < len(diciplinas):
            diciplina_escolhida = diciplinas[escolha]
        else:
            print("Seleção inválida.")
            return
    else:
        print("Nenhuma disciplina cadastrada.")

    dados_turma = {
        "nome": nome_turma,
        "codigo": codigo,
        "disciplina": diciplina_escolhida
    }
    
    turmas.append(dados_turma)
    print("Turma cadastrada com sucesso!")
