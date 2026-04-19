# Exercício 2: Resumo de Folha de Pagamento (Setor de RH)
# Crie uma função chamada calcular_folha que receba 
# o salário bruto de um funcionário. 
# A função deve calcular e retornar dois valores:
# 1. O valor do desconto de impostos (fixado em 10%).
# 2. O salário líquido (salário bruto - desconto).
# Após criar a função, chame-a para um salário de **R$ 5.000,00**, 
# faça o unpacking do retorno e exiba: "Desconto: R$[valor] | Salário Líquido: R$[valor]".

def folha_pagamento(salario):
  desconto = salario * 0.10
  salario_liquido = salario - desconto
  return salario_liquido, desconto


salario_des, desc =folha_pagamento(5000)

print(f'O salário líquido é de R${salario_des} e o desconto foi de R$ {desc}.')