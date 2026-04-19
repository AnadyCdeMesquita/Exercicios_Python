# Exercício 1: Dashboard de Vendas (Análise de Dados)
# Você recebeu uma lista com as vendas 
# diárias de uma equipe: vendas = [1500, 2000, 800, 3500, 1200].
# Crie um programa que exiba um pequeno relatório contendo:
# 1. O total de vendas na semana.
# 2. A média de vendas diária.
# 3. O valor da melhor venda e da pior venda do período.

vendas = [1500, 2000, 800, 3500, 1200]
#SOMA
vendas_total = sum(vendas)
print(vendas_total)

#MÉDIA
media = sum(vendas) / len(vendas)
print(f'{media:.0f}')

#MAIOR E MENOR VENDA

maior = max(vendas)
menor = min(vendas)
print(f'A maior venda é {maior}, a menor venda é  {menor}.')