from resources import mensagem, menu_opcoes
from alunos import cadastar_aluno
from professores import cadastrar_professor
from disciplinas import cadastrar_disciplina
from turmas import cadastrar_turma
from matricular_alunos import matricular_aluno_em_turma
#from alocar_professor import alocar_professor_em_disciplina
# erro circular de importação estou tentando...
from consultas.consultar_alunos_por_turma import consultar_alunos_por_turma
from consultas.consultar_disciplinas_por_turma import consultar_disciplinas_por_turma

# mensagem de boas vindas
mensagem("Sistema Acadêmico")

# dicionário que mapeia as opções do menu com as funções correspondentes
opcoes = {
    1: cadastar_aluno,
    2: cadastrar_professor,
    3: cadastrar_disciplina,
    4: cadastrar_turma,
    5: matricular_aluno_em_turma
    # 6: alocar_professor[...]
}

# Loop principal do programa para interagir com o usuário
def main():
    while True:
        mensagem("Menu Principal")
        menu_opcoes()

        opcao_escolhida = int(input("Digite a opção desejada: "))

        if opcao_escolhida == 1: 
            cadastar_aluno()
        elif opcao_escolhida == 2:
            cadastrar_professor()
        elif opcao_escolhida == 3:
            cadastrar_disciplina() 
        elif opcao_escolhida == 4:
            cadastrar_turma()
        elif opcao_escolhida == 5: 
            matricular_aluno_em_turma()
            print("###### Em teste ######")
            print("###### Em teste ######")
            print("###### Em teste ######")
            # funcionando pronto para implementar
        elif opcao_escolhida == 6:
            print("Não implementado")
            #alocar_professor_em_disciplina()
            print("###### Em teste ######")
            print("###### Em teste ######")
            print("###### Em teste ######")
        elif opcao_escolhida == 7:
            print("Não implementado")
            '''alocar_disciplina'''
        elif opcao_escolhida == 8:
            print("Não implementado")
            '''consultar_professores'''
        elif opcao_escolhida == 9:
            print("###### Em teste ######")
            print("###### Em teste ######")
            print("###### Em teste ######")
            '''consultar_alunos'''
            consultar_alunos_por_turma()
        elif opcao_escolhida == 10:
            print("###### Em teste ######")
            print("###### Em teste ######")
            print("###### Em teste ######")
            '''consultar_disciplinas'''
            consultar_disciplinas_por_turma()
        elif opcao_escolhida == 11:
            print("Saindo do programa...")
            break
        else:
            print("Opção inválida. Tente novamente.")
            
            # os ifs são apenas para testes depois volto com a seleção por dicionário
main()

