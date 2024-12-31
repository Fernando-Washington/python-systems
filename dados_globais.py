# fiquei algumas horas preso em uma "importação circular de módulos" aonde eu importava matricular_alunos para main.py e main.py para matricular_alunos.
# acabei descobrindo da pior forma possível, mas consegui resolver. criando uma variável global para armazenar o valor de matricula_aluno e passando-a como argumento para a função matricular_aluno.

lista_alunos = []
lista_turmas = []
lista_professores = []
lista_disciplinas = []