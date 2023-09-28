import random
import string

# Satunnaisuus

print(random.randint(1,10))

# Nopan heittäminen

print("Silmäluku: "+str(random.randint(1,10)))

# Kolikon heittäminen

print("Tulos: "+random.choice(["kruuna","klaava"]))

# Salasanana arpoj

print("Salasana: "+"".join(random.choices(string.ascii_lowercase, k=8)))

# Sekoittaja

luvut = [1 ,2 ,3 ,4 ,5 ,6 ,7 ,8]

random.shuffle(luvut)

print(luvut)

# Vihollisen sijaininit

vihollisenSijainnit = []

for i in range(0,1000):
    a = str(random.randint(1,100))
    a += ","
    a += str(random.randint(1,100))
    vihollisenSijainnit.append(a)

print(vihollisenSijainnit)

# Listan järjestäminen

lista = [1, 3, 5, 4]

lista.sort()

print(lista) # tulostuu [1, 3, 4, 5]

# Pistelista

pelaajaLista = []
pisteet = -1
while True:
    pelaaja = str(input("Anna pelaaja: "))
    if pelaaja == "lopeta":
        break
    uusiPisteet = int(input("Anna pisteet: "))
    if pisteet == -1:
        pisteet = uusiPisteet
        pelaajaLista.append(pelaaja)
    elif pisteet > uusiPisteet:
        pelaajaLista = []
        pelaajaLista.append(pelaaja)
        pisteet = uusiPisteet
    elif pisteet == uusiPisteet:
        pelaajaLista.append(pelaaja)

print(pelaajaLista,"-",pisteet)