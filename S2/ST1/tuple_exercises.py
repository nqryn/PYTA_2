"""
Tuple (tupla) = structura de date asemanatoare cu o lista, cu diferenta ca tupla
este IMUTABILA, adica odata declara nu o mai putem schimba in nici un fel.
Sintaxa este cu paranteze rotunde ()
"""

t = (1, 2, 3)
print(type(t))
print(t[0])
print(t[1])
print(f'Lungimea tuplei este de {len(t)} elemente')

# t[0] = 7      # va da eroare, nu putem schimba valorile existente
# del t[0]      # va da eroare, nu putem sterge valori

"""
Poate tine orice tipuri de date, le tine ordonat, valorile nu trebuie sa fie unice.
"""
tupla_complexa = (1, 2, True, 1, 2, "string", [100, 101, 102], {0, 100})
print(tupla_complexa)
tupla_complexa[6].append(103)
print(tupla_complexa)

tupla_goala = ()
print(type(tupla_goala))
