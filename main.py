from random import randint
from time import sleep

def dice(): 
    try:
        x = int(input('Enter the lowest possible number : '))
        y = int(input('Enter the highest possible number : '))
        print(randint(x,y))
    except:
        print('Something went wrong, please try again...')
        sleep(1)
        dice()

dice()
