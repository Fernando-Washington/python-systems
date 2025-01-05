from resources import mensagem, menu_opcoes
from alunos import cadastar_aluno
from professores import cadastrar_professor
from disciplinas import cadastrar_disciplina
from turmas import cadastrar_turma
from matricular_alunos import matricular_aluno_em_turma
from alocar_professor import alocar_professor_em_disciplina
from alocar_disciplinas import alocar_disciplina_em_turma

# consultas 
from consultas.consultar_alunos_por_turma import consultar_alunos_por_turma
from consultas.consultar_disciplinas_por_turma import consultar_disciplinas_por_turma
from consultas.consultar_professores_por_disciplina import consultar_professores_por_disciplina

# mensagem de boas vindas
mensagem("Sistema Acadêmico")

# dicionário que mapeia as opções do menu com as funções correspondentes
opcoes = {
    1: cadastar_aluno,
    2: cadastrar_professor,
    3: cadastrar_disciplina,
    4: cadastrar_turma,
    5: matricular_aluno_em_turma,
    6: alocar_professor_em_disciplina,
    7: alocar_disciplina_em_turma,
    8: consultar_professores_por_disciplina,
    9: consultar_alunos_por_turma,
    10: consultar_disciplinas_por_turma,
}

# Loop principal do programa para interagir com o usuário
def main():
    while True:
        mensagem("Menu Principal")
        menu_opcoes()
        try:
            opcao_escolhida = int(input("Digite a opção desejada: "))

            if opcao_escolhida in opcoes:
                opcoes[opcao_escolhida]()
            elif opcao_escolhida == 11:
                print("Saindo do programa...")
                break
            else:
                print("Opção inválida. Tente novamente.")
                
        except ValueError:
                print("Opção inválida. Tente novamente.") 
main()

