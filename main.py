from resources import mensagem, menu_opcoes
from alunos import cadastar_aluno
from professores import cadastrar_professor
from disciplinas import cadastrar_disciplina
from turmas import cadastrar_turma

mensagem("Sistema Acadêmico")

opcoes = {
    1: cadastar_aluno,
    2: cadastrar_professor,
    3: cadastrar_disciplina,
    4: cadastrar_turma
}

while True:
    mensagem("Menu")
    menu_opcoes()

    opcao_escolhida = int(input("Digite a opção desejada: "))

    if opcao_escolhida == 5:
        print("Saindo do sistema...")
        break
    elif opcao_escolhida in opcoes:
        opcoes[opcao_escolhida]()
    else:
        print("Opção inválida. Tente novamente.")
        
        # Se opcao_escolhida estiver em opcoes, a condição é verdadeira e o código dentro do if será executado.

