# Exercício 1: Relatório de Margem de Lucro (Setor Financeiro) 
# Uma empresa de varejo precisa de um resumo
# rápido sobre a performance de um produto. Dado o faturamento de R$ 45.000,00
# e o custo de R$ 23.500,00, crie um programa que calcule o lucro e a margem de lucro
# (lucro dividido pelo faturamento). Exiba uma mensagem formatada onde o lucro use o
# separador de milhar e duas casas decimais,
#  e a margem seja exibida como uma porcentagem inteira.

fat = 45000
custo = 23000
lucro = fat - custo
print(f'O lucro é de R$: {lucro:,.2f}.')

margem_lucro = lucro / fat
print(f'A margem de lucro é de {margem_lucro:.0%}.')

