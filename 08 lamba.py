
add = lambda a,b: a+b
print(add(1,2))


# Cuadrados perfectos
numbers = range(14)
square_numbers = list(map(lambda x:x**2, numbers))
print ("cuadrados:", square_numbers)


#
numbers = range(14)
even_numbers = list(filter(lambda x:x%2==0,numbers))
print(even_numbers)


