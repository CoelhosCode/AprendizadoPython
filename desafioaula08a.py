import math
cateto_adjacente = int(input('Digite o valor do cateto adjacente: '))
cateto_oposto = int(input('Digite o valor do cateto oposto: '))
hipotenusa = math.sqrt(cateto_adjacente*cateto_adjacente + cateto_oposto*cateto_oposto)
print(f'O valor de hipotenusa é {hipotenusa} centimetros.')


