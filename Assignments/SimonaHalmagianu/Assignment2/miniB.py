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

    def adauga_task(self, name, description):
        self.todo[name] = description

    def finalizeaza_task(self, name):
        if name in self.todo:
            del self.todo[name]
            print('Task completed')
        else:
            print('Task missing')

    def afisaza_todo_list(self):
        print(list(self.todo.keys()))

    def afiseaza_detalii_suplimentare(self, task_name):
        if task_name in self.todo:
            print(f'Details for task {task_name}: {self.todo[task_name]}')
        else:
            answer = input(f'The following task {task_name} is not in the list. Do you wish to add it? (yes/no): ')
            if answer.lower() == 'yes':
                description = input("Insert a description for the current task: ")
                self.adauga_task(task_name, description)
                print(f'The task {task_name} has been sucesfully added.')
            else:
                print('Ok, good bye!')


my_tasks = TodoList()
my_tasks.afisaza_todo_list()

my_tasks.adauga_task('Cats', 'Feed')
my_tasks.adauga_task('Car', 'Wash')
my_tasks.afisaza_todo_list()

my_tasks.finalizeaza_task('Shopping')
my_tasks.finalizeaza_task('Car')
my_tasks.afisaza_todo_list()

print('*' * 80)
my_tasks.afiseaza_detalii_suplimentare('Cats')
my_tasks.afiseaza_detalii_suplimentare('Shopping')
my_tasks.afisaza_todo_list()

