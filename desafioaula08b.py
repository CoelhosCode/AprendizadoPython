import math
angulo = float(input('Digite o valor de um angulo: '))
seno = math.sin(math.radians(angulo))
cosseno = math.cos(math.radians(angulo))
tangente = math.tan(math.radians(angulo))
print(f'O valores de seno, cosseno e tangente do numero {angulo} é de: {seno}, {cosseno} e {tangente}')
