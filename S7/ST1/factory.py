"""
Vom implementa următoarele clase:
English/French/Spanish Translator – clase care știu sa traduca cuvinte din română
în limba specificata
- translations va fi un dicționar cu acele cuvinte,
exemplu `{ “masina”: “car” }` – se poate hardcoda în clasa

- localize va fi o funcție care pentru un parametru de intrare,
ne va da traducerea lui în acea limba (exemplu `input(“masina”)` returneaza “car”)

TranslatorFactory – clasa care are o singura metoda
(preferabil statica sau de clasa)
numita get_translator(language) –
in functie de parametrul language, returnează un translator object.

"""
from abc import ABC


class AbstractTranslator(ABC):
    def localize(self, text):
        raise NotImplementedError


class EnglishTranslator(AbstractTranslator):

    def __init__(self):
        self.translations = {
            'masina': 'car',
            'om': 'human',
            'curs': 'course',
            'salut!': 'hello!'
        }

    def localize(self, text):
        if text in self.translations:
            return self.translations[text]
        print('Traducerea nu exista...')


class SpanishTranslator(AbstractTranslator):
    def __init__(self, use_inverted_exclamation_mark=True):
        self.translations = {
            'masina': 'coche',
            'om': 'hombre',
            'curs': 'clase',
            'salut!': 'hola!'
        }
        if use_inverted_exclamation_mark:
            self.translations['salut!'] = '¡hola!'

    def localize(self, text):
        if text in self.translations:
            return self.translations[text]
        print('Traducerea nu exista...')


class FrenchTranslator(AbstractTranslator):
    def __init__(self):
        self.translations = {
            'masina': 'voiture',
            'om': 'homme',
            'curs': 'course',
            'salut!': 'bonjour!'
        }

    def localize(self, text):
        if text in self.translations:
            return self.translations[text]
        print('Traducerea nu exista...')


class TranslatorFactory:
    def __init__(self):
        pass

    @staticmethod
    def get_translator(language):
        if language == 'en':
            return EnglishTranslator()
        elif language == 'es':
            return SpanishTranslator()
        elif language == 'fr':
            return FrenchTranslator()
        else:
            print('Nu exista translator pentru limba ceruta!')


"""
Dupa ce facem acesta structura, in codul meu nu voi mai avea nevoie sa stiu
ce obiect de tipul translator am, deoarece ii voi cere doar clasei Factory
sa imi dea unul gata facut!
"""
translators = []
translators.append(TranslatorFactory.get_translator('en'))
translators.append(TranslatorFactory.get_translator('es'))
translators.append(TranslatorFactory.get_translator('fr'))

for t in translators:
    print(t.localize('masina'))
