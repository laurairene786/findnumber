
import random

def run():
    numero_aleatorio = random.randint(1, 100)
    numero_elegido = int(input('Choose a number from 1 to 100:'))
    while numero_elegido != numero_aleatorio:
        if numero_elegido< numero_aleatorio:
            print('Try with a bigger number')
        else:
            print('try with a smaller number')
        numero_elegido = int(input('Choose a nother number'))
        
    print('You win!')

if __name__ == '_main_':
    run()
    
