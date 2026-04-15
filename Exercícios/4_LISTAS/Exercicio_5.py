# Exercício 5: Atualização de Preços Interativa (Input + Lista)
# Você tem uma lista de preços de
# produtos: precos = [100.0, 250.0, 500.0] 
# e uma com o nome: vinhos = ["Branco", "Tinto","Champagne"].
# Crie um programa interativo que:
# 1. Peça para o usuário digitar qual o nome do produto.
precos = [100.0, 250.0, 500.0] 
vinhos = ["Branco", "Tinto","Champagne"]
valor = float(input('Digite o VALOR do novo vinho: '))
precos.append(valor)
bino = input('Digite o NOME do novo vinho: ')
vinhos.append(bino)
# 2. Peça para o usuário digitar o novo preço.
# 3. Atualize o preço na lista e exiba as listas completas com os nomes e os preços
print(precos)
print(vinhos)

