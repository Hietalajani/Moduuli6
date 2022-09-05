lista = []

while True:
    luku = int(input('Anna luku, -1 lopettaa: '))
    if luku == -1:
        break
    else:
        lista.append(luku)


def funktio(kokonaisluvut):
    print(sum(lista))

funktio(lista)