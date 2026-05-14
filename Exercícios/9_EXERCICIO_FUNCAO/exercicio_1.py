produtos_baguncados = [ " iphone 13 ", "MACBOOK PRO ", " aIrPoDs Pro", "iPad mini "]

def normalizar(texto):
  return texto.strip().capitalize()

#OPCAO 1 COM MAP:
# retorno = list(map(normalizar, produtos_baguncados))
# print(retorno)

#opcao 2

# nova_lista = []
# for produto in produtos_baguncados:
#   produto_padronizado = normalizar(produto)
#   nova_lista.append(produto_padronizado)
# print(nova_lista)

#list compreension

nova_lista = [normalizar(produto) for produto in produtos_baguncados]
print(nova_lista)