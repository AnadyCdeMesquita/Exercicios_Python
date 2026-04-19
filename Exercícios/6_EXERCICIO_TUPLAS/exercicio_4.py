# Exercício 4: Performance de Vendas Regionais (Setor de Dashboard) 
# Crie uma função chamada analisar_vendas que receba uma lista de números (vendas). 
# A função deve retornar o total vendido e a média das vendas. 
# Dado o dicionário
# dados_filiais = {"Matriz": [10000, 15000, 20000], "Filial Sul": [5000, 7000]}:
# 1. Percorra o dicionário.
# 2. Para cada filial, use a função e faça o unpacking do resultado.
# 3. Exiba: "Filial [Nome] -> Total: R$[valor], Média: R$[valor]".




def analisar_vendas(lista_vendas):
  total_vendas = sum(lista_vendas)
  media_vendas = sum(lista_vendas)/ len(lista_vendas)
  return total_vendas, media_vendas

dados_filiais = {"Matriz": [10000, 15000, 20000], "Filial Sul": [5000, 7000]}

for x, filial in dados_filiais.items():
    total, media = analisar_vendas(filial)
    print(f'"Filial {x} -> Total: R${total}, Média: R${media}".')
