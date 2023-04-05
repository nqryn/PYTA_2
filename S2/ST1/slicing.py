"""
Slicing (feliere) = operatia care ne permite sa accesam mai multe elemente dintr-o lista
sau dintr-un string (care este de fapt doar o lista de caractere).
Sintaxa
lista[start:stop:pas] => pas este optional, valoarea lui default este 1
- start reprezinta indexul de la care incepem accesarea, acesta este inclus in valoarea finala
- stop reprezinta indexul la care ne oprim, dar acesata nu este inclus in valoarea finala
- pas (step) reprezinta "viteza" cu care ne miscam de la start la stop, default 1
"""
#    0  1  2  3  4  5  6  7  8
l = [1, 2, 3, 4, 5, 6, 7, 8, 9]
l2 = l[2:5]     # voi obtine elementele din lista originala care sunt la indecsii 2->5, adica [3, 4, 5]
print(l2)

l3 = l[5:2:-1]  # voi obtine [6, 5, 4]
print(l3)

l4 = l[0:len(l):2]  # voi obtine elementele de la indecsii pari
print(l4)

"""
Daca start = inceputul listei (sau finalul daca mergem cu pas negativ) putem sari peste aceasta valoare
Daca stop = sfarsitul listei (sau inceputul daca mergem cu pas negativ) putem sari peste aceasta valoare
"""
l5 = l[::2]     # echivalent cu l4
print(l5)

"""
O metoda foarte simpla de a inversa o lista este sa o parcurgem cu pas de -1
"""
lr = l[::-1]
print(lr)

"""
Deoarece stringurile sunt practic liste de caractere, si la ele se aplica aceleasi reguli 
de slicing!
"""
s = "Ana are mere"
print(s[3:10])
print(s[::2])
print(len(s))
print(s[10:100])    # nu va da eroare, dar vom primi doar caracterele existente pana la sfarsitul stringului

# NU DENUMITI VARIBILELE LIST
list = [100, 200]   # <= DON'T
