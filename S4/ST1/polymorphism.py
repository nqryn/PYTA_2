"""
Polimorfism (poli = mai mult(e), morfos = forme) => ceva ce poate lua mai multe forme.
Se refera la o metoda care poate avea mai multe comportamente, in functie de anumiti factori.

Un prim exemplu de polimorfism este cel vazut in mostenire, atunci cand avem o clasa parinte cu
o metoda doX, iar apoi clasa copil are si el aceeasi metoda doX.
Putem zice ca metoda doX se comporta diferit, in functie de obiectul care o apeleaza (parinte sau copil).

Un alt exemplu de polimorfism este cand avem mai multe functii cu acelasi nume
si cu acelasi comportament, dar cu parametrii diferiti (aici zicem ca facem overloading = supraincarcare)
"""


def add(a, b, c=10):
    return a + b + c


# putem zice ca functia add este polimorfica, deoarece poate fi apelata in mai multe "forme"
print(add(1, 2))
print(add(1, 2, 3))
