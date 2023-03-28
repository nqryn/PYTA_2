"""
Variabila = o locatie din memorie care tine o valoare, si are un nume
1. variabilele au nume unice, pentru a le putea identifica
2. numele de variabile in python sunt valide daca contin litere mici, mari, numere si underscore
3. in general, numele de variabile in python folosesc litere mici si underscore
4. in general, numele de constante in python folosesc doar litere mari si underscore
5. numele de variabile pot incepe cu litere sau _, dar nu cu cifre
6. numele de variabile sunt case-sensitive
IMPORTANT: folositi NUME SUGESTIVE MEREU
"""

varsta_mea = 31  # nume valid, bun
VARSTA_MEA = 31  # nume valid, nu e bun in Python => este de fapt constanta
PI = 3.1415  # nume valid, constanta
VarstaMea = 31  # nume valid, dar nu e bun in Python
# Varsta mea = 31  # nume invalid, deoarece contine spatiu
_variabila_mea = 21  # nume valid, dar nu va recomand sa il folositi acum, deoarece are o semnificatie speciala
# 21variabila = 21  # nume invalid

"""
Le putem schimba valoarea variabilelor pe parcursul unui program (de-aia sunt variabile)
Si chiar si tipul de data pe care acestea o contin
"""
print(varsta_mea)
varsta_mea = 50  # am schimbat valoarea variabilei varsta_mea
print(varsta_mea)

"""
Putem atribui mai multe valori intr-o singura linie:
a, b, c = 10, 20, 30    <= trebuie sa avem potrivire de numar intre numele de variabile si valorile oferite

Sau aceeasi valoare mai multor variabile:
x = y = z = 100
"""
# a, b, c = 10, 20    # va da eroare
# a, b, c = 10, 20, 30, 40    # va da eroare
a, b, c = 10, 20, 30

# Toate cele 3 variabile vor avea *valoarea* 100, dar ele sunt variabile *diferite*
x = y = z = 100
