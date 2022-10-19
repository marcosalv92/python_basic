import random

def run():
    num_random = random.randint(1, 100)
    num_selected = int(input('Adivine el numero: '))
    vidas = 5
    while num_random != num_selected:
        if vidas == 0:
            print('Perdites!! el numero era:'+ str(num_random))
            break
        print('Quedan '+ str(vidas) + ' vidas')
        if num_selected > num_random:
            num_selected = int(input('Elige un numero menor: '))
        else:
            num_selected = int(input('Elige un numero mayor: '))
        vidas -= 1
    
    if num_random == num_selected and vidas != 0:
        print('Adivinaste!!!!')



if __name__ == '__main__':
    run()