# Exercício 3: Análise de Metas de Vendas (Setor Comercial)
# Um gerente quer comparar o desempenho de duas filiais. O programa deve:
# 1. Pedir o faturamento da Loja A e o faturamento da Loja B 
# (o usuário pode digitar números decimais).
# 2. Calcular o faturamento total das duas lojas.
# 3. Calcular a média de faturamento entre elas.
# 4. Exibir uma única mensagem formatada informando o total e a média, 
# utilizando o separador de milhar e duas casas decimais.

fat_a = float(input('DIGITE O FATURAMENTO DA LOJA A: '))

fat_b = float(input('DIGITE O FATURAMENTO DA LOJA B: '))

Fat_Total = fat_a + fat_b

media_fat = (fat_a + fat_b)/2

print(f'O faturamento total é R$ {Fat_Total:,.2f} e a média é:{media_fat:,.2f}')


