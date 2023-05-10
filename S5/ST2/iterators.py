"""
Iterator = un obiect care poate fi iterat. In general, in Python avem colectii iterabile.
Exemple din Python : list, tuple, dict, set, string.


Orice clasa care este iterabila (adica practic o putem parcurge cu un for ... in ...) TREBUIE
sa implementeze doua metode

def __iter__(self):
    -> aici se initializeaza un iterator, adica se foloseste de obicei ceva variabila in care sa se poata
        tine iteratia curenta
        self.contor = 0

def __next__(self):
    -> aici se va returna mereu urmatoarea valoare din colectia iterabila (
    self.contor += 1
    return lista[self.contor]

    -> atunci cand nu mai sunt valori disponibile, metoda next trebuie sa arunce exceptia StopIteration


Aceste 2 metode sunt apelabile din exterior, folosind varianta fara underscores (adica iter() si next() )
"""
l = list([1, 5, 100])

my_iterator = iter(l)   # creez un iterator
print(next(my_iterator))    # va printa 1
print(next(my_iterator))    # va printa 5
print(next(my_iterator))    # va printa 100
# print(next(my_iterator))    # va arunca exceptia StopIteration


"""
Orice clasa care implementeaza cele 2 metode mentionate devine automat iterabila.
Astfel, putem sa ne construim proprii iteratori la nevoie.
Pe langa folosirea lui next, putem sa iteram un iterator folosind for (care este implementat tot cu next())
"""


class AlphabetIterator:
    def __iter__(self):
        self.letter = 'A'
        return self

    def __next__(self):
        current_letter = self.letter
        if current_letter == 'Z':
            raise StopIteration
        self.letter = chr(ord(self.letter) + 1)
        return current_letter


alpha_iter = iter(AlphabetIterator())

# print(next(alpha_iter))
# print(next(alpha_iter))
# print(next(alpha_iter))
# print(next(alpha_iter))     # va arunca exceptie cand ajunge la D

for letter in alpha_iter:
    print(letter)

