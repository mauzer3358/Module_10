from threading import Thread, Lock
from random import randint
from time import sleep

lock = Lock()
class Bank:

    def __init__(self):
        self.balance = 0

    def deposit(self):
        for i in range(0,100):
            up_zapros = randint(50,500)

            if self.balance >= 500 and lock.locked():
                lock.release()
            self.balance = self.balance + up_zapros
            print(f'Пополнение: {up_zapros}.Баланс: {self.balance}\n', end='')
            sleep(0.001)

        ...

    def take(self):
        for j in range(0, 100):
            zapros = randint(50, 500)
            print(f'Запрос на {zapros}\n', end='')

            if zapros > self.balance:
                print(f'Запрос отклонён, недостаточно средств\n', end='')
                lock.acquire()

            elif zapros <= self.balance:
                self.balance = self.balance - zapros
                print(f'Снятие: {zapros}. Баланс: {self.balance}\n', end='')


bk = Bank()

# Т.к. методы принимают self, в потоки нужно передать сам объект класса Bank
th1 = Thread(target=Bank.deposit, args=(bk,))
th2 = Thread(target=Bank.take, args=(bk,))

th1.start()
th2.start()
th1.join()
th2.join()

print(f'Итоговый баланс: {bk.balance}')