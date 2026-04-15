# Exercício 5: Sistema de Triagem de E-mails (Setor de Customer Experience) 
# Crie um sistema que ajude a filtrar para qual departamento uma reclamação deve ir. 
# O usuário deve digitar o assunto do e-mail.
# ● Se no assunto aparecer a palavra "pagamento" ou "boleto", exiba: "Encaminhado para o Financeiro".
# ● Se no assunto aparecer a palavra "entrega" ou "atraso", exiba: "Encaminhado para a Logística".
# ● Caso não seja nenhum desses, exiba: 
# . Dica: Use o operador in para verificar se a palavra está dentro do texto.

assunto = ['pagamento', 'boleto', 'entrega', 'atraso']

palavra = input('DIGITE O ASSUNTO O EM EMAIL:\n').strip()

if palavra in assunto:
  if palavra == 'pagamento' or palavra == 'boleto':
    print("Encaminhado para o Financeiro")
  elif palavra == 'entrega' or palavra == 'atraso':
    print("Encaminhado para a Logística")
  else:
    print('Encaminhado setor geral')
