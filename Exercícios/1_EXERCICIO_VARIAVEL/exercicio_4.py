# Exercício 4: Análise de Margem de Lucro (Financeiro)
# Cenário: Uma consultoria faturou R$ 15.000,00 em um projeto. 
# Os custos fixos foram de R$ 5.000,00 e o imposto sobre o faturamento é de 15%. 
# Objetivo: Calcule o imposto, o lucro líquido e a margem de lucro (Lucro / Faturamento).
# No final, crie uma variável booleana chamada meta_atingida que
#  verifica se a margem de lucro é superior a 0.30 (30%).

faturamento = 15000.00
custos = 5000.00
imposto = 0.15

desconto_imposto = faturamento * imposto
print(f'O valor do desconto pós-imposto é: {desconto_imposto}')

lucro_liquido = faturamento - custos - desconto_imposto
print(f'O lucro líquido é {lucro_liquido}')

margem_lucro = lucro_liquido/faturamento
print(f'Margem de lucro: {margem_lucro:.0%}')

meta_atingida = margem_lucro > 0.30
print(meta_atingida)