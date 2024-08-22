# Tipos numéricos

numero1 = 10
print(numero1)
print(type(numero1))
numero2 = 10.4
print(numero2)
print(type(numero2))
numero3 = 10.4 + 2j
print(numero3)
print(type(numero3))


'''
Strings são objetos do tipo str e
são sequencias imutáveis de códigos Unicode
'''
x = 'oi mundo'
print(x)
print(id(x))
x = 'oi mundo 2'
print(x)
print(id(x))

'''
Lista são objetos mutáveis
'''
lista = ['Carne', 'Pão', 'Sal fino', 'Sal grosso']

''' Tuplas são imutáveis '''
registro1 = ('Orlando Saraiva', 'professor')
print(registro1.count('professor'))

''' Set é um conjunto desordenado de itens hashable'''
c1 = set(list(range(1,10)))
c2 = set(list(range(5,15)))
c3 = set(list(range(7,20)))

print(c1.union(c2))
print(c1.intersection(c2).intersection(c3))
print(c1.difference(c2))

''' Dicionários são mapeamentos'''
lista_telefonica = {}
lista_telefonica['orlando'] = ('Orlando','Saraiva','DW3')
lista_telefonica['nilton'] = ('Nilton','Algoritmo')

for chave in list(lista_telefonica.keys()):
    print(lista_telefonica[chave])

print(lista_telefonica.get('orlando','Não encontrei'))
print(lista_telefonica.get('orlando2','Não encontrei'))
