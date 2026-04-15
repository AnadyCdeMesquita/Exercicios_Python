# Exercício 3: Divisão de Cargas (Logística/Transporte)
# Cenário: Uma transportadora precisa levar 1.250 caixas em 
# caminhões pequenos. Cada caminhão suporta exatamente 12 caixas.
# Objetivo: 1. Quantos caminhões sairão totalmente cheios? (Use //) 
# 2. Quantas caixas sobrarão para serem enviadas em uma última viagem menor? (Use %)

caixas = 1250
caminhao_caixa = 12

caminhao = caixas // caminhao_caixa
print(f'É necessário {caminhao} caminhões.')

transportar = caminhao * caminhao_caixa
print(f"Dará para levar {transportar} caixas")

sobra = caixas % caminhao_caixa
print(f' A sobra de caixa serão {sobra}')