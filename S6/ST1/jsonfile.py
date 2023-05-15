"""
JSON (JavaScript Object Notation) = este o sintaxa asemanatoare cu dictionarele din python,
folosita adesea in comunicarea over the internet. Este un format text pentru schimbul de date.

In formatul JSON, avem obiecte (care sunt cuprinse intre acolade) si Arrays (listele din Python).
Pe langa acestea, avem toate tipurile basic de date : string, int, float, boolean

{"widget": {
    "debug": "on",
    "window": {
        "title": "Sample Konfabulator Widget",
        "name": "main_window",
        "width": 500,
        "height": 500
    },
    "image": {
        "src": "Images/Sun.png",
        "name": "sun1",
        "hOffset": 250,
        "vOffset": 250,
        "alignment": "center"
    },
    "text": {
        "data": "Click Here",
        "size": 36,
        "style": "bold",
        "name": "text1",
        "hOffset": 250,
        "vOffset": 100,
        "alignment": "center",
        "onMouseUp": "sun1.opacity = (sun1.opacity / 100) * 90;"
    }
}}


In JSON, pentru stringuri, folosim mereu double quotes " (ghilimele duble)
Un JSON valid este de fapt un obiect, adica este cuprins intre acolade
"""
import json

with open('files/employees.json') as my_json:
    # putem citi fisierul json si linie cu linie, daca vrem, DAR pierdem toata informatia primita din formatarea sa
    employees = json.load(my_json)
    print(type(employees))

    for e in employees['employees']:
        print(e['name'])

"""
La fel cum putem "incarca" un JSON intr-un dictionar, putem face si operatiunea inversa, adica putem scrie
din dictionar, intr-un fisier de tip JSON.
"""

dict_complex = {
    'id': 1,
    'name': ['Adela', 'Neacsu'],
    'height': 1.80,
    'course': {
        'name': 'Python + Testare automata',
        'start date': '27 martie 2023'
    }
}
with open('files/newj.json', 'w') as newj:
    json.dump(dict_complex, newj, indent=4)

"""
CSV = comma separated values

id,name,age
1,Adela,31
2,Ionut,25
3,Ion Popescu,45
"""
