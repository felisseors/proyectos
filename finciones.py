suma = 1
divicion = 2

run = input('que operacion quieres hacer 1 = suma, 2 = divicion')

def suma (a,b):
    a = int(input('escoge un numero'))
    b = int(input('cual es tu edad'))
        total = a + b
        return total

def divicion (a,b):
    a = int(input('escoge un numero'))
    b = int(input('cual es tu edad'))
        total = a / b
        return total
        
if run == '1':
    print(suma(a,b))

elif run == '2':
    print(divicion(a,b))
    
       
    
