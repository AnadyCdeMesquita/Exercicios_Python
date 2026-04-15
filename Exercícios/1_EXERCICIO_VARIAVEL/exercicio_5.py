# Exercício 5: Conversão de Tempo de Contrato (Gestão de Projetos)
# Cenário: Um contrato de manutenção de software tem a duração de 40 meses.
# O cliente quer ver esse tempo no formato: "X anos e Y meses".
# Objetivo: Utilize os operadores de divisão inteira e resto da divisão
# para converter os 40 meses.

meses = 40
ano = 12
anos = meses// ano
print(f'Será de {anos} anos.')

anos2 = meses % ano
print(f'Será de {anos2} meses.')

print(f'')
