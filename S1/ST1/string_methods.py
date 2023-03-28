"""
len(s) => ne da lungimea unui string, adica nr de caractere
"""
s = "Hello, world"
print(len(s))   # 12, se numara tot, inclusiv spatii, taburi, newline
ss = " \n"
print(len(ss))  # 2, adica un spatiu, si un newline

"""
Metode pe stringuri:
metodele sunt niste functii care se apeleaza pe o anumita variabila:

nume_var.nume_metoda()
"""
print(s.count('l'))     # numara cate caractere l avem in string
print(s.lower())        # converteste stringul la lowercase
print(s.upper())        # converteste stringul la uppercase

"""
Tema: treceti prin metodele de la string, si vedeti ce fac fiecare.
"""