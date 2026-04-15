# Exercício 3: Cálculo de Desconto Progressivo (Setor de Vendas) 
# Um e-commerce aplica descontos automáticos no carrinho.
# Crie um programa que receba o valor total da compra e aplique a seguinte lógica:
# ● Compras a partir de R$ 500,00: 15% de desconto.
# ● Compras a partir de R$ 200,00 (e menos de 500): 10% de desconto.
# ● Compras abaixo de R$ 200,00: Sem desconto.
# O programa deve exibir o valor do desconto e o valor final a pagar, formatados em R$.

valor = input('Digite o valor total a ser pago: ').strip().replace('.', '').replace(',','.')
valor = float(valor)
desconto1 = (valor * 0.15)
desconto2 = (valor * 0.10)

if valor >= 500.00:
  print(f'O valor do desconto é R$ {desconto1:,.2f} e valor final é R$ {valor - desconto1:,.2f}.')
elif valor >= 200.00:
  print(f'O valor do desconto é R$ {desconto2:,.2f} e valor final é R$ {valor - desconto2:,.2f}.')
else:
  print(f'R$ {valor:,.2f} não tem desconto.')
