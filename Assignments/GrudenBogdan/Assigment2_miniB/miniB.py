"""
TodoList
    Atribute: todo (dict, cheia e numele taskului, valoarea e descrierea)
La început nu avem taskuri, dict e gol

     Metode:
adauga_task(nume, descriere) - se va adauga in dict
finalizează_task(nume) - se va sterge din dict
afișează_todo_list() - doar cheile

Ramane ca TEMA (nu modificati fisierul acesta, faceti unul la voi in folder):
afișează_detalii_suplimentare(nume_task) - în funcție de numele taskului, printăm detalii suplimentare.
    Dacă taskul nu e în todo list, întrebam utilizatorul dacă vrea să-l adauge.
    Dacă acesta răspunde nu - la revedere
    Dacă răspunde da - îi cerem detalii task și salvăm nume+detalii în dict
"""

class TodoList:
    def __init__(self):
        self.todo = {}      # dictionar gol

    def adauga_task(self, nume, descriere):
        self.todo[nume] = descriere

    def finalizeaza_task(self, nume):
        if nume in self.todo:
            del self.todo[nume]
            print('Taskul a fost finalizat')
        else:
            print('Taskul nu exista in lista')

    def afiseza_todo_list(self):
        print(list(self.todo.keys()))

    def afiseaza_detalii_suplimentare(self, nume_task):
        if nume_task in self.todo:
            print(f'Detalis for {nume_task} are: {self.todo.get(nume_task)}')
        else:
            print(f'The task {nume_task} is not in our ToDo list')
            adauga = input(f'Would you like to add: {nume_task} in our list?')
            if adauga == 'no':
                print('Goodbye')
            else:
                detalii = input(f'Add more detalis about the {nume_task}')
                self.todo[nume_task] = detalii
                print('The updated list:')
                for key, value in self.todo.items():
                    print(f" {key} : {value}\n")



lista1 = TodoList()
lista1.afiseza_todo_list() #Afisam lista goala!
lista1.adauga_task('Task1', 'Terminat proiect MiniB') #Adaugam primul task!
lista1.afiseza_todo_list() #Afisam lista dupa ce am adaugat primul task.
lista1.finalizeaza_task('Task1') #Stergem task-ul.
lista1.afiseza_todo_list() #Afisam lista dupa ce am sters task-ul.

print('_' * 80) #Testam functia afiseaza detalii suplimentare.
lista1.adauga_task('Task1', 'Termiant proiect MiniB') #Adaugam primul task!
lista1.afiseza_todo_list()
lista1.afiseaza_detalii_suplimentare('Task1') #Afisam detaliile doar daca task-ul este in lista.
lista1.afiseaza_detalii_suplimentare('Task2') #Testam daca task-ul nu e in lista.