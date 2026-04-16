import random
import math

proizvodi = [
    "Laptop",
    "Mis",
    "Tastatura",
    "Monitor",
    "Slusalice",
    "Web kamera",
    "USB memorija",
    "Stampac"
]

cene = {
    "Laptop": 950.99,
    "Mis": 19.99,
    "Tastatura": 49.99,
    "Monitor": 199.99,
    "Slusalice": 89.99,
    "Web kamera": 59.99,
    "USB memorija": 14.99,
    "Stampac": 129.99
}

print("Lista proizvoda i cena:")
for proizvod in proizvodi:
    print(proizvod, "-", format(cene[proizvod], ".2f"), "€")


budzet = float(input("\nUnesite svoj budzet u evrima: "))

print("\nProizvodi koje mozete da priustite:")
for proizvod in proizvodi:
    if cene[proizvod] <= budzet:
        print(proizvod, "-", format(cene[proizvod], ".2f"), "€")


def najskuplji_proizvod(recnik_cena):
    najskuplji = max(recnik_cena, key=recnik_cena.get)
    return najskuplji

najskuplji = najskuplji_proizvod(cene)
print("\nNajskuplji proizvod je:", najskuplji, "-", format(cene[najskuplji], ".2f"), "€")

nasumican_proizvod = random.choice(proizvodi)
print("\nKorisniku je privukao paznju proizvod:", nasumican_proizvod)

zbir_cena = sum(cene.values())
prosecna_cena = zbir_cena / len(cene)
prosecna_cena = math.floor(prosecna_cena * 100 + 0.5) / 100

print("\nProsecna cena svih proizvoda je:", format(prosecna_cena, ".2f"), "€")

prodati_komadi = [5, 20, 12, 7, 10, 8, 30, 4]

ukupan_prihod = 0
for i in range(len(proizvodi)):
    ukupan_prihod += cene[proizvodi[i]] * prodati_komadi[i]

print("\nUkupan prihod je:", format(ukupan_prihod, ".2f"), "€")

novi_proizvod = "Tablet"
nova_cena = 299.99

proizvodi.append(novi_proizvod)
cene[novi_proizvod] = nova_cena

print("\nAzurirana lista proizvoda:")
for proizvod in proizvodi:
    print(proizvod, "-", format(cene[proizvod], ".2f"), "€")

sortirani_proizvodi = sorted(cene.items(), key=lambda x: x[1])

print("\nProizvodi sortirani od najjeftinijeg ka najskupljem:")
for proizvod, cena in sortirani_proizvodi:
    print(proizvod, "-", format(cena, ".2f"), "€")

