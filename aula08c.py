import random
aluno_1 = str(input('Digite o nome de do primeiro aluno: '))
aluno_2 = str(input('Digite o nome do segundo aluno: '))
aluno_3 = str(input('Digite o nome do terceiro aluno: '))
aluno_4 = str(input('Digite o nome do quarto aluno: '))
lista = [aluno_1, aluno_2, aluno_3, aluno_4]
escolhido = random.sample(lista, k=4)
print(f'O aluno escolhido foi: {escolhido}')