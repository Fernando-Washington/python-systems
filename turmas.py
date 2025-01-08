from dados_globais import lista_turmas, lista_disciplinas
from resources import gerar_codigo, mensagem
    # nome codigo carga horaria professor 

# cadastro de turmas
def cadastrar_turma():
    """função que cadastra turmas e armazena os dados na lista_turmas
    """
    mensagem("Cadastro de Turmas")
    
    nome_turma = input("Digite o nome da turma: \n")
    codigo = gerar_codigo()
    
    if lista_disciplinas:
        print("Disciplinas disponíveis:")
        for i, item in enumerate(lista_disciplinas):
            print(f"{i + 1} - {item['nome']}")
        escolha = int(input("Selecione o número da disciplina: \n")) - 1
        if 0 <= escolha < len(lista_disciplinas):
            disciplina_escolhida = lista_disciplinas[escolha]
        else:
            print("Seleção inválida.")
            return
    else:
        print("Nenhuma disciplina cadastrada.")

    nova_turma = {
        "nome": nome_turma,
        "codigo": codigo,
        "alunos": [], # lista vazia para armazenar alunos matriculados
        "disciplina": [],
    }
    
    lista_turmas.append(nova_turma)
    print("Turma cadastrada com sucesso!")
