from random import randint
from threading import Lock, Thread
from time import sleep


class Bank:
    def __init__(self):
        self.balance = 0
        self.lock = Lock()

    def deposit(self):
        for i in range(100):
            i = randint(50, 500)
            self.balance += i
            print(f'"Пополнение: {i}. Баланс: {self.balance}".')
            if self.balance >= 500 and self.lock.locked():
                self.lock.release()
            sleep(0.001)

    def take(self):
        for i in range(100):
            i = randint(50, 500)
            print(f'Запрос на {i}')
            if i <= self.balance:
                self.balance -= i
                print(f'"Снятие: {i}. Баланс: {self.balance}".')
            else:
                print('Запрос отклонён, недостаточно средств')
                self.lock.acquire()
            sleep(0.001)


bk = Bank()

th1 = Thread(target=Bank.deposit, args=(bk,))
th2 = Thread(target=Bank.take, args=(bk,))

th1.start()
th2.start()
th1.join()
th2.join()

print()
print(f'Итоговый баланс: {bk.balance}')
