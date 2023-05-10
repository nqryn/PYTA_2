"""
Decorators = functii speciale care ne permit sa augmentam alte functii.
Putem face anumite actiuni folosind decoratorii atat inainte, cat si dupa apelarea functiei decorate
Sintaxa de folosire:
@decorator
def nume_functie_decorata(....):

Sintaxa de implementare:
def decorator_func(decorated_func):
    def inner_func():
        # actiuni inainte de apelarea functiei decorate
        decorated_func()
        # actiuni DUPA functia decorata

    return inner_func
"""


def print_hi_and_bye(func):
    def inner_func():
        print("Hi")
        func()      # apelam functia originala!!
        print("Bye")
    return inner_func

@print_hi_and_bye
def say_hello():
    print("Hello, I am a function")

@print_hi_and_bye
def introduce_yourself():
    print("Hi, my name is Adela, and this is Python!")


say_hello()
introduce_yourself()

"""
De ce folosim decoratori? In general, pentru a aduga o anumita functionalitate in mai multe locuri.
Exemplu din Django -> decoratorul de login_required
DRY = Don't Repeat Yourself

@login_required
def view_all_products():
    ....

"""

print('_' * 80)

"""
Pentru a decora functii cu parametrii, avem nevoie sa stim si de existenta parametrilor in decorator.
"""

def decadd(func):
    def inner(*args, **kwargs):    # aici avem nevoie de acelasi nr de param ca si functia originala
        print("Adding stuff...")
        print(f'Positional params: {args}')
        print(f'Keyword params: {kwargs}')
        result = func(*args, **kwargs)     # aici trebuiie sa apelam functia originala cu parametrii primiti,
        # si sa nu uitam sa returnam rezultatul la final
        print("Done adding stuff")
        return result
    return inner

def introduce(func):
    def inner_func(*args, **kwargs):
        print("Hi")
        result = func(*args, **kwargs)
        print("Bye")
        return result
    return inner_func


@decadd
def add2(a, b):
    return a + b

@decadd
def add3(a, b, c):
    return a + b + c

@decadd
@introduce
def add4(a, b, c=0, d=100):
    return a + b + c + d


print(add2(10, 17))
print(add3(1, 2, 4))
print(add4(1, 2, c=5))      # echivalent cu decadd(introduce(add4(1, 2, c=4))

"""
args = arguments, sau parametrii pozitionali ai unei functii. Atunci cand nu stim exact
cati parametrii pozitionali va avea o functie, pasam *args, deoarece acei parametrii vor fi 
"impachetati" intr-o tupla numita args, iar folosind steluta, facem operatiunea de despachetare.
Packing / Unpacking

kwargs = keyword arguments, adica parametrii NUMITI ai unei functii. Acestia sunt "impachetati"
sub forma unui dictionar, si sunt despachetati folosind doua stelute.
"""

"""
Sintaxa finala a unui decorator (care functioneaza cu orice tipuri de functii)

def decorator(func_originala):
    def inner(*args, **kwargs):
        ... pre-procesare [optional]
        result = func_originala(*args, **kwargs)
        ... post-procesare [optional]
        return result
    return inner
"""

"""
Exemplu de login required (luat din Flask)

def login_required(func):
    def wrapper_login_required(*args, **kwargs):
        if g.user is None:
            return redirect(url_for("login", next=request.url))
        return func(*args, **kwargs)
    return wrapper_login_required
"""

"""
Putem avea mai multi decoratori pentru aceeasi functie!
Chaining = inlantuire a decoratorilor, adica acestia se apeleaza pe rand, de sus in jos.

@dec1
@dec2
def func(...):
    ...
    
    
Apelarea unei functii decorate ar fi echivalent cu:
dec1 ( dec2 ( func () ))


@login_required
@user_is_admin
def view_products():
    ....

"""
