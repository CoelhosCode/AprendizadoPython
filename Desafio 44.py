preço_compras = float(input('Preço das compras: R$'))
print('''FORMAS DE PAGAMENTO
[1] À vista dinheiro/pix
[2] Cartão à vista
[3] 2x No cartão
[4] 3x ou mais no cartão''')
opcao = int(input('Qual é a opção? '))
if opcao == 1:
    novo_preco = preço_compras - (preço_compras * 0.10)
elif opcao == 2:
    novo_preco = preço_compras - (preço_compras * 0.05)
elif opcao == 3:
    novo_preco = preço_compras
    parcela = preço_compras / 2
    print(f'Sua compra será parcelada em 2x de R${parcela:.2f}')
elif opcao == 4:
    novo_preco = preço_compras + (preço_compras * 0.20)
    total_parcelas = int(input('Quantas parcelas? '))
    parcela = novo_preco / total_parcelas
    print(f'Sua compra será parcelada em {total_parcelas}x de R${parcela:.2f} COM JUROS!')
print(f'Sua compra de R${preço_compras:.2f} vai custar R${novo_preco:.2f} no final!')