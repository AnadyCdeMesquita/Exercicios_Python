# Exercício 2: Calculadora de Imposto Sobre Serviço - ISS (Setor Fiscal) Crie uma função 
# chamada calcular_iss que receba o valor de um serviço. 
# ●  Se o valor for maior que R$ 5.000,00, a taxa é de 5%. 
# ●  Caso contrário, a taxa é de 3%. A função deve retornar o valor do imposto (e não o 
# valor total). Depois, use essa função para calcular o imposto de uma nota de R$ 
# 8.000,00 e outra de R$ 2.000,00, exibindo os resultados

def iss(valor):
  if valor > 5000:
    return valor * 0.05
  else:
    return valor * 0.03
  
print(iss(8000))
print(iss(2000))