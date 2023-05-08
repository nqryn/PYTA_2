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

    def afisaza_todo_list(self):
        print(list(self.todo.keys()))

    def afiseaza_detalii_suplimentare(self, nume_task):
        if nume_task in self.todo:
            print(f'Detaliile sunt {nume_task}: {self.todo[nume_task]}')
        else:
            answer = input(f'Acest task {nume_task} nu este in lista. Doriti sa il adaugati? (Da/Nu): ')
            if answer.lower() == 'da':
                description = input("Adaugati o descriere pt acest task: ")
                self.adauga_task(nume_task, description)
                print(f'Task-ul {nume_task} a fost adaugat.')
            else:
                print('La revedere')

my_tasks = TodoList()
my_tasks.afisaza_todo_list()

my_tasks.adauga_task('task1', 'Curatenie')
my_tasks.adauga_task('task2', 'Teme')
my_tasks.afisaza_todo_list()

my_tasks.finalizeaza_task('task3')
my_tasks.finalizeaza_task('task2')
my_tasks.afisaza_todo_list()

my_tasks.afiseaza_detalii_suplimentare("Plimbare")