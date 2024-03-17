Preco = float(input('Qual o valor do produto? '))
Desconto = Preco * (5 / 100)
NovoPreco = Preco - Desconto
print('O produto custava R${:.2f} com 5% de desconto, irá custar R${:.2f}'.format(Preco, NovoPreco))
