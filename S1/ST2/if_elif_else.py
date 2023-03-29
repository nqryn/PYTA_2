"""
if (daca) ne permite noua sa decidem daca o anumita bucata de cod se executa sau nu
Sintaxa

if conditie:
    acest cod
    va fi executat
    atata timp cat codul este INDENTAT corect
....
"""
age = 19
print("Inainte de if")

if age > 18:
    # liniile acestea indentate se vor executa doar daca conditia (age > 18) este adevarata
    print("Esti major")
    print("Felicitari!")

print("Dupa if")
print("_" * 80)

"""
else (altfel) - functioneaz doar impreuna cu if, si este blocul de cod ce se va
executa atunci cand conditia este falsa

if conditie:
    bloc de cod IF
else:
    bloc de cod ELSE
"""

nota_trecere = 5
nota_primita = int(input("Introdu nota primita:\n"))
if nota_primita >= nota_trecere:
    print("Felicitari, ai trecut!")
    print("Blocul IF s-a terminat...")
else:
    print("Din pacate, ai picat, revino in toamna!")
    print("Blocul ELSE s-a terminat")

print("_" * 80)

"""
Putem avea oricate nivele de imbricare pentru if-uri, DAR
trebuie sa decidem cat inseamna prea mult
Rule of thumb: 3 nivele de indentare sunt suficiente, daca sunt necesare mai multe,
ar trebui gasita alta solutie
"""
if age >= 18:
    print("esti major")
    if age >= 65:
        print("Esti pensionar")
        if age > 100:
            print("Felicitari, esti centagenar")
    else:   # daca varsta este mai mica de 65
        print("esti adult, dar nu pensionar")

"""
elif (else-if)

if conditie1:
    cod executat cand conditie1 este adevarat
elif conditie2:
    cod executat cand conditie2 este adevarat
elif conditie3:
    cod executat cand conditie3 este adevarat
....
else:
    cod executat cand niciuna dintre conditiile de mai sus nu sunt adevarate
"""
years_of_experience = int(input("Introdu anii de experienta:\n"))

if years_of_experience < 0:
    print("Ai gresit valoarea....")
else:
    if years_of_experience == 0:
        # aici va intra doar daca yoe este 0
        print("Esti intern, poti merge la un internship")
    elif years_of_experience < 3:
        # aici va intra doar daca yoe este 1 sau 2
        print("Esti junior, salariul tau este 4000")
    elif years_of_experience < 5:
        # aici va intra doar daca yoe este 3 sau 4
        print("Esti mid, salariul tau este 8000")
    elif years_of_experience < 10:
        # aici va intra doar daca yoe este 5 - 9 (inclusiv)
        print("Esti senior, salariul tau este 12000")
    else:
        # aici va intra doar daca yoe este 10 sau mai mare
        print("Felicitari, esti pensionat!")
