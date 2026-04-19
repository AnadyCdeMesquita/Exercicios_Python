# Exercício 3: Processamento de Vendas por Unidade (Setor Comercial)
# Você tem uma lista de tuplas onde cada tupla representa uma 
# venda: vendas_dia = [("Monitor", 900, 2), ("Teclado", 150, 5), ("Mouse", 80, 10)]. 
# Cada tupla contém (produto, preco_unitario, quantidade).
# Crie um loop for que use unpacking diretamente na estrutura do loop para extrair
#  os três valores e, para cada item, imprima: "Produto: [nome] | Total: R$[preco * quantidade]".

vendas_dia = [("Monitor", 900, 2), ("Teclado", 150, 5), ("Mouse", 80, 10)]
soma = 0
for produto, preco_unitario, quantidade in vendas_dia:
  soma += preco_unitario * quantidade
  print(f'Produto:{produto} e total preço R$ {preco_unitario * quantidade}')

print(f'A soma total é R$ {soma}')
