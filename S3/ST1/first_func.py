# pret_masini = {
#     'Dacia': 6800,
#     'Lăstun': 500,
#     'Opel': 1100,
#     'Audi': 19000,
#     'BMW': 23000
# }
# buget = 15000
# for masina, pret in pret_masini.items():
#     if pret <= buget:
#         print(f'Masina {masina} costa {pret} si se incadreaza in buget')

"""
Daca vreau sa obtin masinile in functie de buget, dar NU STIU de la inceput bugetul,
ma ajuta sa pot sa "apelez" acest cod doar cand am eu nevoie.

De asemenea, daca vreau sa ofer masini in functie de buget pentru mai multi oameni diferiti,
ma ajuta sa pot sa folosesc acest cod de mai multe ori.
"""

"""
Functie = o bucata de cod, care are un nume* si pe care noi o putem folosi ori de cate ori vrem.
Sunt relativ asemanatoare cu functiile din matematica (exemplu f(x) = 2*x+5)
f - numele functiei
x - parametrul functiei, adica un nume de variabila pe care noi il folosim in interiorul functiei,
dar care primeste o valoare atunci cand apelam functia; exemplu f(5), f(100)
rezultat - valoarea returnata de o functie; exemplu f(5) => 15, f(100) => 205 
"""

"""
Sintaxa:
def nume_functie(param1, param2, ... paramX):
    aici
    facem
    tot
    ce
    vrem
    cu
    functia
    
"""
# nu putem apela o functie inainte ca aceasta sa fie definita
# f(200) # NameError: name 'f' is not defined

def f(x):
    print(f'Sunt in functia f!')
    print(f'Am primit parametrul {x}')
    print(f'Gata, acum iesim din functie. Bye bye!\n')

print('Azi invatam despre functii!')

"""
Apelarea unei functii, adica invocarea codului respectiv, se face folosind numele functiei respective,
urmat de paranteze rotunde, si eventuali parametrii.
"""
f(5)
f("Adela")