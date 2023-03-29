# """
# 10.Transformă și printează notele din sistem românesc în >
# Peste 9 => A
# Peste 8 => B
# Peste 7 => C
# Peste 6 => D
# Peste 4 => E
# 4 sau sub => F
# """
#
# grade = float(input("Introdu nota:\n"))
# american_grade = ""
#
# """
# In general, input checks sunt PRIMELE chestii pe care le facem:
# fail-fast, adica daca utilizatorul a introdus date gresite, vrem sa "scapam"
# de acest use-case cat mai repede.
# """
#
# if grade > 10 or grade <= 0:
#     print("Ai introdus o valoare gresita!")
# else:
#     if grade <= 4:
#         american_grade = "F"
#     elif grade < 6:
#         american_grade = "E"
#     elif grade < 7:
#         american_grade = "D"
#     elif grade < 8:
#         american_grade = "C"
#     elif grade < 9:
#         american_grade = "B"
#     else:
#         american_grade = "A"
#     # afisam mesajul doar daca nota introdusa a fost corecta!
#     print(f"Felicitari, ai luat nota {american_grade}")


"""
14.      x, y, z (int)
Afișează care este cel mai mare dintre ele?
"""
x = int(input("Introdu x:\n"))
y = int(input("Introdu y:\n"))
z = int(input("Introdu z:\n"))

"""
Evitati sa folositi max, min, sum, ca si nume de variabile in python,
deoarece sunt functii, si daca le folosim ca nume de variabile,
nu le mai putem folosi ca functii (se face shadowing)
"""
# maxi = x     # presupunem ca valoarea maxima este x
# if maxi < y:
#     maxi = y
# if maxi < z:
#     maxi = z
# print(f"Valoarea maxima este {maxi}")
# print(f"Verificare: {max(x, y, z)}")

"""
Solutia 2: fara folosirea unei variabile auxiliare!
"""
# if x >= y and x >= z:
#     print(x)
# elif y >= x and y >= z:
#     print(y)
# else:
#     print(z)

"""
Solutia 3: cu if-uri imbricate si fara variabila aux
"""
if x >= y:
    # aici il comparam pe x cu z, deoarece y sigur nu este cel mai mare
    if x >= z:
        print(x)
    else:
        print(z)
else:
    # aici il comparam pe y cu z, deoarece x sigur nu este cel mai mare
    if y >= z:
        print(y)
    else:
        print(z)
