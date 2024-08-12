from threading import Thread
from random import randint
from time import sleep
import queue


class Table:
    def __init__(self, number, guest=None):
        self.number = number
        self.guest = guest


class Guest(Thread):
    def __init__(self, name):
        super().__init__()
        self.name = name

    def run(self):
        sleep(randint(3, 10))


class Cafe:
    def __init__(self, *tables):
        self.queue = queue
        self.tables = tables

    def guest_arrival(self, *guests):
        for guest in guests:
            for table in tables:
                table.guest = guest
                print(f"{guest.name} сел(-а) за стол номер {table.number}")
                break

    def discuss_guests(self):
        pass


# # Создание столов
tables = [Table(number) for number in range(1, 6)]
# # Имена гостей
guests_names = ['Maria', 'Oleg', 'Vakhtang', 'Sergey', 'Darya', 'Arman',
                'Vitoria', 'Nikita', 'Galina', 'Pavel', 'Ilya', 'Alexandra']
# # Создание гостей
guests = [Guest(name) for name in guests_names]
# # Заполнение кафе столами
cafe = Cafe(*tables)
# # Приём гостей
cafe.guest_arrival(*guests)
# # Обслуживание гостей
# cafe.discuss_guests()
