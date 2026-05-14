# Exercício 5: Conversor de Moeda Interativo (Setor de Importação) A empresa precisa 
# converter preços de uma lista em Dólar para Real. 
# 1.  Crie uma função chamada converter_para_real que receba um preço em dólar 
# e a cotação do dia, retornando o valor em real. 
# 2.  Crie uma segunda função chamada processar_lista_precos que receba uma 
# lista de preços em dólar e a cotação. Dentro dela, use a primeira função para 
# calcular o valor de cada item e exiba: "O item custa R$[valor]". Teste com a lista 
# e cotação de 5.20.

# Função 1: converte dólar para real
def converter_para_real(preco_dolar, cotacao):
    valor_real = preco_dolar * cotacao
    return valor_real

# Função 2: processa uma lista de preços
def processar_lista_precos(lista_precos, cotacao):
    for preco in lista_precos:
        valor_em_real = converter_para_real(preco, cotacao)
        print(f"O item custa R${valor_em_real:.2f}")

# Testando o programa
precos_dolar = [10, 25, 50, 100]  # lista de preços em dólar
cotacao = 5.20

processar_lista_precos(precos_dolar, cotacao)