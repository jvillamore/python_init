#diccionarios
claves = {"key1":"value", "key2":"value2"}
print(claves)
print(claves.keys())
print(claves.values())
print(claves.items())

celsius=[0, 10,20, 30,40,50]
farenheit = [(temp * 9/5)*32 for temp in celsius]
print(farenheit)
far2 = [x**2 for x in range(1,5) if x%2 ==0 ]
print(far2) 

matrix = [[1,2,3],[4,5,6],[7,8,9]]
transposed = [[row[i] for row in matrix] for i in range(len(matrix[0]))]

print (matrix)
print (transposed)
