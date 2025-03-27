#listas
lista = ['a','b','c']
print(lista)
print(id(lista))
lista.append('d')
print(lista)
listaB = lista.copy()
listaB.remove('a')
listaB.extend([1,2,3])
print(listaB)
del listaB[2]
print(listaB)
