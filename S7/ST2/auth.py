import requests

body = {
    "username": "Adela",
    "password": "helloWorld"
}
auth_response = requests.post("https://dummyjson.com/auth/login", data=body)
print(f'Status code : {auth_response.status_code}')
print(auth_response.json())

print('=' * 80)
body = {
    "username": "atuny0",
    "password": "9uQFF1Lh"
}
auth_response = requests.post("https://dummyjson.com/auth/login", data=body)
print(f'Status code : {auth_response.status_code}')
print(auth_response.json())

correct_response = auth_response.json()
"""
De obicei, atunci cand avem un request de login/auth, vom primi un token, care mai apoi trebuie sa fie setat
in headere pentru orice requesturi subsecvente, pentru ca serverul sa stie cine suntem noi.
"""
auth_token = correct_response['token']

"""
Header = sunt niste metainformatii pe care serverul si clientul le schimba intre ei, pentru a stii cum sa comunice.
Exemple de headere:
ACCEPT - clientul ii zice serverului ce fel de formate stie sa accepte (json, xml, etc)
Authorization - este un header in care clientul poate trimite un token, astfel incat serverul sa stie sa il autorizeze 
    pentru un anumit request.
Location - serverul ii zice clientului unde este locatia unei anumite resurse (de obicei pe status codes de 3xx) 
"""

headers = {
    'Authorization': f'Bearer {auth_token}'
}
