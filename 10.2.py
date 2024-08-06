from threading import Thread
from time import sleep


class Knight(Thread):

    def __init__(self, name: str, power: int):
        self.name = name
        self.power = power
        super().__init__()

    def run(self):
        print(f"{self.name}, на нас напали!")
        enemy = 100
        day = 0
        for i in range(self.power):
            enemy -= i
            if enemy <= 0:
                print(f"{self.name} одержал победу спустя {day} дней(дня)!")
        day += 1
        print(f"{self.name} сражается {day}..., осталось {enemy} воинов.")
        sleep(1)


first_knight = Knight("Sir Lancelot", 10)
second_knight = Knight("Sir Galahad", 20)

thread_1 = first_knight
thread_2 = second_knight

thread_1.start()
thread_2.start()

thread_1.join()
thread_2.join()
