"""
2. Aceeași listă:
mașini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lăstun', 'Fiat', 'Trabant', 'Opel']

Folosește un for else
În for
Modifică elementele din listă astfel încât să fie scrise cu majuscule, exceptând primul și ultimul.
În else:
  Printează lista.
"""
cars = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lăstun', 'Fiat', 'Trabant', 'Opel']
# ca sa pot modifica lista, am nevoie de indecsii acesteia, asa ca for-ul meu va fi pe indecsi

# for idx in range(len(cars)):
#     print(f'{idx}: {cars[idx]}')

# cars[0] = cars[0].upper()   # asa fac un element al listei sa devina scris cu masjuscule

for idx in range(len(cars)):
    if idx == 0 or idx == len(cars) - 1:    # daca indexul este 0 sau len-1 (Adica daca suntem la primul SAU ultimul element
        continue    # sarim peste
    cars[idx] = cars[idx].upper()   # transformam masina de la indexul idx in majuscule
else:
    print(cars)


"""
6. Având dict:
pret_masini = {
    'Dacia': 6800,
    'Lăstun': 500,
    'Opel': 1100,
    'Audi': 19000,
    'BMW': 23000
}

Vine un client cu un buget de 15000 euro.
Prezintă doar mașinile care se încadrează în acest buget.
"""
pret_masini = {
    'Dacia': 6800,
    'Lăstun': 500,
    'Opel': 1100,
    'Audi': 19000,
    'BMW': 23000
}
buget = 15000
for masina, pret in pret_masini.items():
    if pret <= buget:
        print(f'Masina {masina} costa {pret} si se incadreaza in buget')
