import random

max = int(input('Anna nopan maksimisilmäluku: '))

def nopanheitto(summa):
    while True:
        luku = random.randint(1, max)
        print(f'Silmäluku: {luku}')
        if luku == max:
            return

nopanheitto()