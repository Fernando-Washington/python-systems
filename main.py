from resources import mensagem, menu_opcoes
from alunos import cadastar_aluno
from professores import cadastrar_professor
from disciplinas import cadastrar_disciplina
from turmas import cadastrar_turma

# mensagem de boas vindas
mensagem("Sistema Acadêmico")

# dicionário que mapeia as opções do menu com as funções correspondentes
opcoes = {
    1: cadastar_aluno,
    2: cadastrar_professor,
    3: cadastrar_disciplina,
    4: cadastrar_turma
}

# Loop principal do programa para interagir com o usuário
def main():
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
main()

