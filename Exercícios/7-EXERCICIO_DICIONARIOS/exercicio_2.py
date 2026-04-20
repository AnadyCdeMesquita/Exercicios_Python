# Exercício 2: Consulta de Estoque Interativa (Setor de Logística)
# A empresa possui o seguinte estoque:
# estoque = {"teclado": 50, "mouse": 120, "monitor": 30}. 
# Crie um programa que peça para o usuário digitar o nome de um produto.
# 1. Se o produto existir no estoque, exiba a quantidade disponível.
# 2. Se o produto não existir, exiba a mensagem: 
# "Produto não encontrado no sistema".
# Dica: Lembre-se de tratar o input para evitar erros de letras maiúsculas ou espaços.

estoque = {"teclado": 50, "mouse": 120, "monitor": 30}

produto = input('Digite o nome do produto: ').lower().strip()
if produto in estoque:
  print(f'Há o produto {produto}, e o estoque é {estoque[produto]}')
else:
  print("Produto não encontrado no sistema")
