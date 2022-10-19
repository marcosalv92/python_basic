def run():
    # nombre = input('Escribe tu nombre: ')
    # for letra in nombre:
    #     if letra == ' ':
    #         continue
    #     print(letra.upper())

    for contador in range(1000):
        if contador % 2 != 0:
            continue
        print(contador)

if __name__ == '__main__':
    run()