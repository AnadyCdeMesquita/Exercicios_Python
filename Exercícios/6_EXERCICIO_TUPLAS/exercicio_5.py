# Exercício 5: Gestão de Chamados de Suporte (Setor de TI) O sistema de chamados
# precisa de um resumo diário. Crie uma função resumo_chamados que receba uma lista
# com tempos de resposta (em minutos). Ela deve retornar a quantidade de chamados e 
# o tempo máximo de espera.
# Teste a função com a lista tempos = [15, 45, 10, 120, 30].
# Desempacote os resultados e exiba uma mensagem formatada alertando 
# sobre o tempo máximo encontrado.



def resumo_chamados(tempo_resposta):
  qtde_chamados = len(tempo_resposta)
  tempo_maximo = max(tempo_resposta)
  return qtde_chamados, tempo_maximo

tempos = [15, 45, 10, 120, 30]
qtde, maximo = resumo_chamados(tempos)
print( f'A quantidade é {qtde} e a media total é {maximo}.')