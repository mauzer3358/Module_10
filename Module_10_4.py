import time
from threading import Thread
import queue
from time import sleep
from random import randint

class Table:
    def __init__(self, number):
        self.table_number = number
        self.guest = None

class Guest(Thread):
    def __init__(self, name):
        super().__init__()
        self.name = name

    def run(self):
        time.sleep(randint(3,10))



# Класс Cafe:
#
# Объекты этого класса должны создаваться следующим способом - Cafe(Table(1), Table(2),....)
# Обладать атрибутами queue - очередь (объект класса Queue) и tables - столы в этом кафе (любая коллекция).
# Обладать методами guest_arrival (прибытие гостей) и discuss_guests (обслужить гостей).

class Cafe:
    def __init__(self, *tables):
        self.queue = queue.Queue()
        self.tables = tables
        #print('table', self.tables)

    def guest_arrival(self, *guests):
        for i in guests:
            #print(i.name)
            free_table = [t for t in self.tables if t.guest is None]
            #print('free', free_table)
            if len(free_table)>0:
                free_table[0].guest = i
                i.start()
                print(f'{free_table[0].guest.name} сел(-а) за стол {free_table[0].table_number}')
            else:
                self.queue.put(i)
                print(f'{i.name} в очереди')

# Обслуживание должно происходить пока очередь не пустая(метод empty) или хотя бы один стол занят.
# Если за столом есть гость(поток) и гость(поток) закончил приём пищи(поток завершил работу - метод is_alive),
# то вывести строки "<имя гостя за текущим столом> покушал(-а) и ушёл(ушла)" и "Стол номер <номер стола> свободен".
# Так же текущий стол освобождается(table.guest = None).
    # Если очередь ещё не пуста(метод empty)
# и стол один из столов освободился(None), то текущему столу присваивается гость взятый из очереди(queue.get()).
# Далее выводится строка "<имя гостя из очереди> вышел(-ла) из очереди и сел(-а) за стол номер <номер стола>"
# Далее запустить поток этого гостя(start)

    def discuss_guests(self):
        while not self.queue.empty() or len([t for t in self.tables if t.guest is not None])>0:
            for busy_table in [t for t in self.tables if t.guest is not None]:
                if (busy_table.guest is not None) and not busy_table.guest.is_alive():
                    print(f'{busy_table.guest.name} покушал(-а) и ушёл(ушла)')
                    print(f'Стол номер {busy_table.table_number} свободен')
                    busy_table.guest = None
                    free_table = [t for t in self.tables if t.guest is None]
                    #print('free',free_table[0].table_number)
                    if not self.queue.empty() and len(free_table)>0:
                        free_table[0].guest = self.queue.get()
                        #print('queue',free_table[0].guest)
                        print(f'{free_table[0].guest.name} вышел(-ла) из очереди и сел(-а) за стол номер {free_table[0].table_number}')
                        free_table[0].guest.start()



        ...



# Создание столов
tables = [Table(number) for number in range(1, 6)]
#print(tables[0].table_number)
#Имена гостей
guests_names = [
'Maria', 'Oleg', 'Vakhtang', 'Sergey', 'Darya', 'Arman',
'Vitoria', 'Nikita', 'Galina', 'Pavel', 'Ilya', 'Alexandra'
]
# Создание гостей
guests = [Guest(name) for name in guests_names]

# # Заполнение кафе столами
cafe = Cafe(*tables)
# # Приём гостей
cafe.guest_arrival(*guests)
# # Обслуживание гостей
cafe.discuss_guests()
