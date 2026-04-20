# Exercício 3: Análise de Faturamento por Região (Setor Financeiro) 
# Dada a lista de faturamento por região:
# vendas_regiao = {"Norte": 15000, "Sul": 22000, "Leste": 18000, "Oeste": 25000}. 
# Seu programa deve:
# 1. Extrair todos os valores (faturamentos) para uma lista.
# 2. Calcular e exibir o faturamento total da empresa (soma de todas as regiões).
# 3. Calcular e exibir o faturamento médio das regiões.

vendas_regiao = {"Norte": 15000, "Sul": 22000, "Leste": 18000, "Oeste": 25000}

# nova_lista = list(vendas_regiao.values())
# print(nova_lista)
# valor_total = sum(nova_lista)
# media = valor_total / len(nova_lista)
# print(f'O valor total é {valor_total:,.2f} e a média é {media:,.2f}')

soma_total = sum(vendas_regiao.values())
print(soma_total)
media_total = soma_total / len(vendas_regiao)

print(f'{soma_total:,.2f}, {media_total:,.2f}')

  