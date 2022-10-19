objetivo = int(input('Escoge un entero: '))
epsilon = 0.0001
bajo = 0
alto = max(1.0, objetivo)
respuesta = (bajo + alto)/2

while abs(respuesta**2 - objetivo) >= epsilon:
    print(f'bajo = { bajo }, alto = { alto }, respuesta = {respuesta}')
    if (respuesta ** 2 > objetivo):
        alto = respuesta
    else:
        bajo = respuesta
    respuesta = (bajo + alto)/2

print(f'La raiz cuadrada de {objetivo} es {respuesta}')

