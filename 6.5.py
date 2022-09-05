lista = []
uusilista = []

while True:
    luku = int(input('Anna luku, -1 lopettaa: '))
    if luku == -1:
        break
    else:
        lista.append(luku)

def parittomatpois(parametri):
    for numero in lista:
        if numero % 2 != 0:
            uusilista.append(numero)
        else:
            continue

parittomatpois(lista)
print(f'Vanha lista on: {lista}.')
print(f'Uusi parempi pariton lista on: {uusilista}.')
