import time
from threading import Thread
from time import sleep

class Knight(Thread):


    def __init__(self, sir, power):
        self.res = []
        self.sir = sir
        self.power = power
        self.enemy = 100
        super().__init__()


    def run(self):
        print(f'{self.sir}, на нас напали!\n', end='')
        while self.enemy >= self.power:
            self.enemy = self.enemy - self.power
            time.sleep(1.0)
            self.res.append(self.enemy)
            print(f'{self.sir} сражается {len(self.res)} дней , осталось {self.enemy} воинов.\n', end='')
        print(f'{self.sir} одержал победу спустя {len(self.res)} дней(дня)!')

first_knight = Knight('Sir Lancelot', 10)
second_knight = Knight("Sir Galahad", 20)

threads = []
sirs = [first_knight,second_knight]
for i in sirs:
    thread = i
    thread.start()
    threads.append(thread)

for thread in threads:
    thread. join()

print('Все битвы закончились')