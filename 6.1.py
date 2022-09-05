import random

def nopanheitto():
    while True:
        luku = random.randint(1, 6)
        print(f'Silmäluku: {luku}')
        if luku == 6:
            return

nopanheitto()