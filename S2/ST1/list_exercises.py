"""
Lista (list) = o structura de date Python care poate contine orice alte tipuri de date,
si care este delimitata de paranteze drepte, iar elementele ei sunt delimitate de virgula.
"""

l = [1, 2, 3, 10]
print(type(l))  # <class 'list'>

"""
Pentru a lucra cu elemente individuale din lista, folosim accesarea directa,
adica prin index. Indexarea incepe de la 0 !!
"""
print(l[0])     # primul element din lista, adica numarul 1
print(l[1])     # al doilea element din lista, adica numarul 2
print(l[3])     # al patrulea element din lista, adica nr 10

"""
Pentru a stii cate elemente aveam intr-o lista, folosim functia len.
"""
print(f'Lista mea are {len(l)} elemente')
print(f'Deci indexul ultimului element va fi len(l) - 1')
print(f'Iar acel element poate fi accesat cu formula {l[len(l) - 1]}')

"""
Deoarece putem scrie lista[len(lista) - 1] pentru a gasi ultimul element,
Python are o sintaxa speciala care ne permite sa nu mai punem partea cu len(l),
adica putem folosi indecsi negativi
"""
print(f'Ultimul element este {l[-1]}')
print(f'Penultimul element este {l[-2]}')

# print(l[-5])  # va da eroare, IndexError: list index out of range
# print(l[4])  # va da eroare, IndexError: list index out of range

"""
Listele sunt mutabile - adica le putem modifica atat prin schimbarea elementelor existente,
cat si prin adaugarea unora noi, sau stergerea celor care sunt deja in lista.
"""
print('_' * 80)
print(l)
l[2] = 7    # schimb valoarea celui de-al treilea element din lista din 3 in 7
print(l)

l.append(15)    # asa adaugam un element nou la finalul listei
print(l)

l.insert(3, 100)    # asa inseram un element unde vrem noi, insert(index, element) => inserarea se face inaintea indexului dat ca parametru
print(l)

last = l.pop()     # pop va sterge ultimul element din lista daca nu ii dam nici un argument
print(l)
first = l.pop(0)    # sau va sterge elementul de la indexul mentionat, daca ii dam un argument
print(l)
print(f'Am sters ultimul {last} si primul {first}')

"""
Listele:
- sunt mutabile (Adica le putem modifica)
- pot tine ORICE tipuri de date
- sunt accesibile prin index
- indexarea incepe de la 0, si se termina la len(l) - 1
- putem sa le accesam si cu indecsi negativi
- pot tine inclusiv valori duplicate
"""
print('_' * 80)
list_strings = ['Adela', 'este', 'trainer la cursul de Python']
print(list_strings[0])  # va printa 'Adela'
print(list_strings[0][0])   # va printa 'A'
print(list_strings[0][1])   # va printa 'd'

lista_complexa = [
    1,
    2,
    'cartof',
    True,
    ['alta', 'lista', 7],
    100,
    True,
    True,
    1,
    []
]
lista_goala = []
print(lista_complexa[4])    # lista interioara este un singur element
print(lista_complexa[4][0]) # va printa 'alta'
