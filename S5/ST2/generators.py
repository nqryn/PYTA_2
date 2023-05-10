"""
Generatori = o modalitate simpla de a genera valori care pot fi parcurse secvential.
Dpdv al sintaxei, generatorii sunt functii care folosesc cuvantul cheie yield pentru a da inapoi o valoare
codului care i-a apelat.

Spre deosebire de o functie normala, care ori de cate ori este apelata, ea va fi executata de la inceput,
generatorii vor continua dupa yield.

Yield = a ceda prioritate
"""

def func_gen():
    print("Am intrat in functia generator")
    yield 10        # aici functia noastra generator va returna o valoare (10)

    print("Am intrat DIN NOU in functia generator") # la a doua apelare, se va continua de aici
    yield 100       # a doua valoare returnata

    print("Am intrat a 3a oara in functia generator")

gen = func_gen()
print(next(gen))
print(next(gen))
# print(next(gen))    # va da eroare StopIteration, deoarece nu ajunge la nici o instructiune yield

"""
Generatorii sunt foarte utili, deoarece ei pot "crea" valori noi la fiecare apelare, 
si consuma putina memorie.
Spre deosebire de iteratori, generatorii pot rula la infinit (desi nu e indicat).
De asemenea, sunt mult mai usor de implementat decat iteratorii.
"""

# generator care imi genereaza patrate perfecte
def pp(limit=10):
    p = 0
    while p < limit:
        yield p ** 2
        p += 1

gen_pp = pp()
print('_' * 80)
print(next(gen_pp))
print(next(gen_pp))
print(next(gen_pp))
print(next(gen_pp))
print(next(gen_pp))
print("Incepem FOR")

for val in gen_pp:  # ATENTIE : aici vom intra in bucla infinita !!!!
    print(val)

# Daca vrem sa o luam de la 0, TREBUIE sa facem un nou generator, nu avem cum sa mergem inapoi