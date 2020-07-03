operacion = int(input('escoge una operacion 1,2 multi, 3,4 rest'))

if operacion == 1 or operacion == 2:

    n = int(input(''))
    f = int(input('* ')) 
    def multiplicador(n):
        print(n)
        if n < 0:
            -n * (-f) 

        return n * (n)
    print(multiplicador(n))

elif operacion == 3 or operacion == 4:

    n = int(input(''))
    f = int(input('- '))
    def resta(n):

        return n - (f)
    print(resta(n))

else:
    print('numero invalido, regresa cuando estes mas tranqui')
    



