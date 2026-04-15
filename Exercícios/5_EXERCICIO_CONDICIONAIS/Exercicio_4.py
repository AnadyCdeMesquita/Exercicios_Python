# Exercício 4: Análise de Metas Combinadas (Setor Comercial) 
# Uma empresa paga bônus se a meta individual do vendedor E a meta da loja forem batidas.
# 1. Peça as vendas do vendedor e a meta individual dele.
# 2. Peça as vendas totais da loja e a meta da loja.
# 3. Se o vendedor bater a meta dele E a loja bater a meta total, o bônus é de 20% sobre as vendas do vendedor.
# 4. Caso contrário, o bônus é zero. Exiba a mensagem: "Seu bônus este mês é de: R$[valor]".

vendas_vendedor = 5000
metas_vendedor = 6000

total_vendas = 80000
metas_lojas = 50000

if metas_vendedor >=vendas_vendedor and total_vendas >=metas_lojas:
  print(f'O vendedor receberá R$ {(vendas_vendedor * 0.20):,.2f}.')
else:
  print('Bônus Zero')