def enum():
    objetivo = int(input("Escoge un número entero: "))
    respuesta = 0   
    while respuesta**2 < objetivo:
        print (respuesta)
        respuesta += 1   
    if respuesta**2 == objetivo:
        return print(f'La raíz cuadrada de {objetivo} es {respuesta}')
    else:
        return print(f'{objetivo} no tiene una raíz cuadrada exacta')
    
def busbi():
    objetivo = int(input("Elige un Número: "))
    epsilon = 0.01
    bajo = 0.0
    alto = max(1.0, objetivo)
    respuesta = (alto+ bajo)/2

    while abs(respuesta**2 - objetivo)>= epsilon:
        if respuesta**2 < objetivo:
            bajo = respuesta
        else:
            alto = respuesta
            respuesta = (alto+bajo)/2
    return print(f'La raíz cuadrada de {objetivo} es {respuesta}')

def aprox_sol():
    objetivo = int(input("Elige un Número: "))
    epsilon = 0.01
    paso = epsilon**2
    respuesta = 0.0
    while abs(respuesta**2 - objetivo) >= epsilon and respuesta <= objetivo:
        respuesta += paso
    if (respuesta**2 - objetivo) >= epsilon:
        return
    else:
        return print(f'La raíz cuadrada de {objetivo} es {respuesta}')

                  
                 
select = int(input("Escribe el número correspondiente al algoritmo que deseas elegir:\n 1 para Enumeración Exhaustiva \n 2 para Búsqueda Binaria\n 3 para Aproximación de Soluciones \n Escribe tu selección aquí: "))
if select == 1:
    print("Has elegido el algoritmo de Enumeración Exhaustiva")
    enum()
elif select == 2:
    print("Has elegido el algoritmo de Busqueda Binaria")
    busbi()
elif select == 3:
    print("Has elegido el algoritmo de Aproximación de Soluciones")
    aprox_sol()
else:
    print("Elegiste una opción inválida, vueve otro día con más calmita.")