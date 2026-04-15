# Exercício 2: Padronização de Dados de CRM (Setor de Vendas) Um vendedor cadastrou 
# um cliente com os dados desorganizados no 
# sistema: nome = " mArCoS aNtOnIo rOcHa " 
# e email = " MARCOS.ROCHA@GMAIL.COM ". 
# Para evitar duplicidade e erros de envio, você deve:
# 1. Remover os espaços extras no início e fim das duas variáveis.
# 2. Deixar o nome apenas com as primeiras letras de cada palavra em maiúsculo (formato de nome próprio).
# 3. Deixar o e-mail todo em letras minúsculas. Exiba os resultados finais no console.

nome = 'mArCoS aNtOnIo rOcHa'
nome2= nome.title().strip()
print(nome2)

email = " MARCOS.ROCHA@GMAIL.COM "
email2 = email.strip().lower()
print(email2)

