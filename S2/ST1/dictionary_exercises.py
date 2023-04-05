from pprint import pprint
"""
Dictionary (dictionar) = o structura de date de tipul cheie - valoare,
cu mentiunea ca cheile trebuie sa fie unice!
Sintaxa:
{
    cheie1: valoare1,
    cheie2: valoare2,
    cheieX: valoareX
}
"""
d = {
    'dictionary': 'dictionar',
    'car': 'masina',
    'programming': 'programare'
}

train = {
    'white': 'rocks',
    'red': 'iron',
    'blue': 'cereals',
    'yellow': 'rocks',
    'pink': 'rocks'
    # 'white': ''   # nu pot avea chei duplicate
}

"""
Un dictionar se acceseaza la fel ca si o lista, cu diferenta ca aici nu avem indecsi,
asa ca accesam elementele pe baza cheilor.
"""
print(train['white'])   # va printa 'rocks'
print(train['red'])

"""
Daca folosim numere intregi incepand cu 0 intr-un dictionar, este la fel ca si o lista
"""
dict_as_list = {
    0: 'Ana',
    1: 'are',
    2: 'mere'
}
my_list = ['Ana', 'are', 'mere']
print(dict_as_list[0], my_list[0])

"""
In valorile dictionarelor putem pune orice tipuri de date,
dar cheile sunt putin mai restrictionate:
- putem folosi strings, ints, floats, booleans (toate tipurile basic)
- NU putem folosi o lista ca si cheie
- NU putem folosi un alt dictionar ca si cheie
- NU putem folosi un set ca si cheie
- PUTEM folosi o tupla ca si cheie
Practic, cheile unui dictionar pot fi doar tipuri de date imutabile
"""
db = {
    True: "acesta este true",
    False: "acesta este false",
    # True: ""  # nu putem repeta cheile
}

dictionar_gol = {}

dict_complex = {
    'id': 1,
    'name': ['Adela', 'Neacsu'],
    'height': 1.80,
    'course': {
        'name': 'Python + Testare automata',
        'start date': '27 martie 2023'
    }
}
print(dict_complex['name'][0])  # va printa 'Adela'
print(dict_complex['name'][1])  # va printa 'Neacsu'
print(dict_complex['course']['name'])   # va printa 'Python + Testare automata'

"""
Pentru a afla dimensiunea unui dictionar, folosim len
Dictionarile sunt mutabile (adica le putem schimba, adauga/sterge valori)

"""
print('_' * 80)
print(len(dict_complex))
dict_complex['id'] = 10  # schimbarea valorii se face prin atribuirea unei noi valori pe vechea cheie
dict_complex['age'] = 31    # adaugarea unui nou element (cheie-valoare)
pprint(dict_complex)

del dict_complex['course']  # stergerea unui element din dictionar
pprint(dict_complex)

"""
Putem vedea toate cheile unui dictionar folosind metoda keys()
Putem vedea toate valorile unui dictionar folosind metoda values()
Putem verifica daca o cheie exista intr-un dictionar inainte de a cere valorea acesteia folosind get
Putem sterge toate elementele dintr-un dictionar folosind metoda clear()
"""
print(dict_complex.keys())
print(dict_complex.values())
# print(dict_complex['course'])   # va da eroare KeyError: 'course'
print(dict_complex.get('course'))   # va da None, o valoare speciala Python care reprezinta absenta valorii
dict_complex.clear()    # va sterge toate elementele din dictionar
pprint(dict_complex)    # va afisa {}, adica dictionarul gol
