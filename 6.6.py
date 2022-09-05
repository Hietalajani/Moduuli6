import math

halkaisija = []
hinta = []
wortit = []

for n in range(2):
    halk = int(input(f'Anna pizzan {n+1} halkaisija senttimetreinä: '))
    hint = int(input(f'Anna pizzan {n+1} hinta euroina: '))
    halkaisija.append(halk)
    hinta.append(hint)

def wortti(halka, eur):
    for i in halkaisija:
        ala = (halkaisija / 2) * math.pi ** 2 / 100
        eurperneliö = hinta / ala
        print(f'Pizzan neliöhinta on {eurperneliö}.')
        wortit.append(eurperneliö)
        nimi[i] = Pizza[i]

# wortti(halkaisija[0], hinta[0])
# wortti(halkaisija[1], hinta[1])
wortti(halkaisija, hinta)

print(wortit)

wortit.sort()
print(f'Parempi vastine rahalle: {wortit[0]}.')
