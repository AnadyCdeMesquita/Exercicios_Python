# Exercício 2: Gestão de Estoque (Edição e Verificação) 
# Uma loja de eletrônicos possui os seguintes 
# produtos: estoque = ["monitor", "teclado", "mouse", "headset"]. 
# O gerente pediu para:
# 1. Adicionar o item "webcam" ao final da lista.
# 2. O "teclado" teve seu nome atualizado para "teclado mecanico".
# Faça essa alteração na lista.
# 3. Verificar se "impressora" está no estoque. 
# O programa deve exibir True ou False.
# 4. Remover o "mouse" da lista, pois saiu de linha.

estoque = ["monitor", "teclado", "mouse", "headset"]
#1-Adicionar o item "webcam" ao final da lista.
estoque.append("webcam")
print(estoque)
#2-O "teclado" teve seu nome atualizado para "teclado mecanico".
estoque[1] = "teclado mecanico"
print(estoque)
#3-Verificar se "impressora" está no estoque.
impressora = 'impressora' in estoque
print(impressora)

#4. Remover o "mouse" da lista, pois saiu de linha.
remover = estoque.pop(2)
print(estoque)
