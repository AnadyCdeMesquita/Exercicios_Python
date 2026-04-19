# Exercício 4: Sistema de Logística (Busca e Extensão)
#  A empresa "LogTrack" tem uma rota de entregas:
#  rota = ["Sao Paulo", "Campinas", "Jundiai", "Sorocaba"].
#  Novas cidades foram adicionadas por uma empresa parceira: 
# novas_cidades = ["Itu", "Valinhos"]. Seu script deve:
# 1. Unir as duas listas em uma só (usando extend).
rota = ["Sao Paulo", "Campinas", "Jundiai", "Sorocaba"]
novas_cidades = ["Itu", "Valinhos"]
rota.extend(novas_cidades)
print(rota)
# 2. Identificar em qual posição (índice) está a cidade de "Sorocaba".
posicao = rota.index("Sorocaba")
print('Posição:', posicao)
# 3. Exibir a lista completa e a posição encontrada.
# 4. Exibir uma mensagem final: “Sorocaba é a Xª cidade da rota”
print(f'Sorocaba é a {posicao}ª cidade da rota ')