"""
TodoList
    Atribute: todo (dict, cheia e numele taskului, valoarea e descrierea)
La început nu avem taskuri, dict e gol și nu avem nevoie de constructor

     Metode:
adauga_task(nume, descriere) - se va adauga in dict
finalizează_task(nume) - se va sterge din dict
afișează_todo_list() - doar cheile
afișează_detalii_suplimentare(nume_task) - în funcție de numele taskului, printăm detalii suplimentare.
Dacă taskul nu e în todo list, întrebam utilizatorul dacă vrea să-l adauge.
Dacă acesta răspunde nu - la revedere
Dacă răspunde da - îi cerem detalii task și salvăm nume+detalii în dict

"""

class TodoList:

    def __init__(self, nume_lista):
        self.nume_lista = nume_lista
        self.tasks = {}
        self.isdone = False

    def adauga_task(self, nume, descriere):
        self.tasks[nume] = descriere

    def finalizeaza_task(self,nume_task):
        print(f"Task-ul {nume_task} a fost sters")
        del self.tasks[nume_task]

    def afiseaza_todo_list(self):
        if self.tasks:
            print("My To do List:")
            for task in self.tasks.keys():
                print(task)
        else:
            print("My To do List este goala")

    def afiseaza_detalii_suplimentare(self, nume_task):
        print(f"Detalii suplimentare pentru {nume_task}: {self.tasks[nume_task]}")


todo = TodoList("Curatenie")
todo.afiseaza_todo_list()
todo.adauga_task(1, 'Sterge praful')
todo.afiseaza_todo_list()
todo.afiseaza_detalii_suplimentare(1)
todo.finalizeaza_task(1)
todo.afiseaza_todo_list()

