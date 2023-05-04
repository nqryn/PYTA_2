"""
Mașină
Atribute: marca, model, viteza maximă, viteza_actuală, culoare, culori disponibile (set), înmatriculată (bool)
   Culoare = gri - toate mașinile când ies din fabrică sunt gri
   Viteza_actuală = 0 - toate mașinile stau pe loc când ies din fabrică
   Culori disponibile = alege tu 5-7 culori
   Marca = alege tu - fabrica produce o singură marcă, dar mai multe modele
   Înmatriculată = False
Constructor: model, viteza_maxima
Metode:
descrie() - se vor printa toate atributele, în afară de culori_disponibile
înmatriculare() - va schimba atributul înmatriculată în True, si se va da un numar de inmatriculare
vopsește(culoare) - se va vopsi mașina în noua culoare DOAR dacă noua culoare e în opțiunea de culori disponibile,
    altfel afișați o eroare
accelerează(viteza) - se va accelera la o anumită viteză, dacă viteza e negativă-eroare,
    dacă viteza e mai mare decât viteza_max - masina va accelera până la viteza maximă
franeaza() - mașina se va opri și va avea viteza 0
"""

class Masina:
    # variabile de clasa (acestea sunt comune tuturor obiectelor SI nu se pot schimba)
    __MARCA = 'Mercedes'
    CULORI_DISPONIBILE = ('ROSU', 'BLUE', 'GRI', 'ALB')

    def __init__(self, model, viteza_max):
        # aici avem variabile de instanta, ele exista doar cand facem un obiect
        self.model = model
        self.viteza_max = viteza_max
        self.__culoare = 'GRI'
        self.viteza_act = 0
        self.__inmatriculata = False
        self.__nr_inmatriculare = None    # putem folosi si '',dar None este mult mai ok

    """
    Nu facem setteri pentru inmatriculata si nr_inmatriculare, deoarece acestea ar trebui sa se poata modifica
    DOAR prin intermediul metodei de inmatriculare(), pentru a evita eventualele discrepante de atribute.
    """
    @property
    def inmatriculata(self):
        return self.__inmatriculata

    @property
    def nr_inmatriculare(self):
        return self.__nr_inmatriculare

    @property
    def marca(self):
        return Masina.__MARCA

    @property
    def culori_disponibile(self):
        return Masina.CULORI_DISPONIBILE

    def descrie(self):
        print(f'{self.marca} {self.model} {self.culoare}')
        print(f'Viteza : {self.viteza_act} / {self.viteza_max}')
        if self.inmatriculata:
            print(f'Masina este inmatriculata cu numarul {self.nr_inmatriculare}')
        else:
            print('Masina NU este imatriculata')

    def inmatriculare(self, nr_inmatriculare):
        self.__inmatriculata = True
        self.__nr_inmatriculare = nr_inmatriculare

    def vopseste(self, culoare):
        if culoare in self.culori_disponibile:
            self.__culoare = culoare
        else:
            print('Culoarea nu e disponibila')

    @property
    def culoare(self):
        return self.__culoare

    @culoare.setter
    def culoare(self, culoare):
        if culoare in self.culori_disponibile:
            self.__culoare = culoare
        else:
            print('Culoarea nu e disponibila')

    def accelereaza(self, viteza):
        if viteza < 0:
            print('Eroare, viteza nu poate fi negativa')
        elif viteza > self.viteza_max:
            self.viteza_act = self.viteza_max
        else:
            self.viteza_act = viteza

    def franeaza(self):
        self.viteza_act = 0

m1 = Masina('clasa S', 220)
print(m1.CULORI_DISPONIBILE)    # aici accesam direct variabila de clasa, care este mostenita la toate obiectele
print(m1.culori_disponibile)    # aici accesam proprietatea, care de fapt ne da tot variabila de clasa
print(m1.marca)
print(Masina.CULORI_DISPONIBILE)     # nu am nevoie de un obiect ca sa accesez variabilele de clasa

print('_' * 80)
m1.descrie()
# m1.vopseste('VERDE')        # nu va merge
# m1.vopseste('ROSU')
m1.culoare = 'VERDE'
m1.inmatriculare('CJ22ITF')
print()
m1.descrie()
m1.culoare = 'ROSU'
print()
m1.descrie()
