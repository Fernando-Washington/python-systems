from resources import gerar_codigo
    # nome codigo carga horaria professor
turma = []  
    
def cadastrar_turma():
    print(" 4 - Cadastrar Turma")
    nome_turma = input("Digite o nome da turma: \n")
    codigo = gerar_codigo()
    
    # queria que essa parte possuisse a opção de escolher a disciplina ja cadastrada e vincular a turma a ela de alguma forma, não só nessa funcao mas nas outras tambem
    
    print("Disciplinas disponíveis:")
    
    '''listar_opcoes(diciplinas, "nome", "codigo")'''
    
    nome_professor = input("Digite o nome do professor responsável: \n")
    dados_turma = {}
    
    dados_turma["nome"] = nome_turma
    dados_turma["codigo"] = codigo
    '''dados_turma["disciplina"] = diciplina_escolhida["codigo"],'''
    dados_turma["professor"] = nome_professor
    
    turma.append(dados_turma)
    
    print("Turma cadastrada com sucesso!")
    print(dados_turma) # placeholder
    
    # nome codigo disciplina professor alunos (lista-matricula)


    
    
   # - Crie um sistema escolar que permita cadastrar alunos, professores, disciplinas e turmas.