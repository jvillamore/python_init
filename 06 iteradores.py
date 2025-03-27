# Iteradores
text = 'hola munde'
my_iter = iter(text)

for char in my_iter:
    print(char)

# Generadores
def my_generator():
    yield 'a'
    yield 'b'
    yield 'c'

for val in my_generator():
    print(val)
    
# Generadores
def fibonacci(limit):
    a, b = 0, 1
    while a< limit:
        yield a
        a,b = b, a+b

for fib in fibonacci(15):
    print(fib)