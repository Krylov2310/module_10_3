import threading
from random import randint
from threading import Lock
from time import sleep

print('\033[30m\033[47mДомашнее задание по теме "Блокировки и обработка ошибок"\033[0m')
print('\033[30m\033[47mЗадача "Банковские операции":\033[0m')
print('\033[30m\033[47mСтудент Крылов Эдуард Васильевич\033[0m')
thanks = '\033[30m\033[47mБлагодарю за внимание :-)\033[0m'
print()


# Исходный код:
class Bank:
    def __init__(self):
        self.balance: int = 0
        self.lock = Lock()
        self.str_balance = []

    def deposit(self):
        for tranzakcia in range(100):
            if self.balance >= 500 and self.lock.locked():
                self.lock.release()
            biliberda: int = randint(50, 500)
            self.balance += biliberda
            a1 = f'Пополнение: \033[34m{biliberda}\033[0m. Баланс: \033[32m{self.balance:}\033[0m'
            self.str_balance.append(a1)
            sleep(0.001)

    def take(self):
        for request in range(100):
            biliberda: int = randint(50, 500)
            a2 = f'Запрос на \033[35m{biliberda}\033[0m.'
            self.str_balance.append(a2)
            if biliberda <= self.balance:
                self.balance -= biliberda
                a3 = f'Снятие: \033[33m{biliberda}\033[0m. Баланс: \033[32m{self.balance}\033[0m.'
                self.str_balance.append(a3)
                sleep(0.001)
            else:
                a4 = f'\033[31mЗапрос откланен, недостаточно средств.\033[0m'
                self.str_balance.append(a4)
                self.lock.acquire()
                sleep(0.001)


bk = Bank()

# Т.к. методы принимают self, в потоки нужно передать сам объект класса Bank
th1 = threading.Thread(target=Bank.deposit, args=(bk,))
th2 = threading.Thread(target=Bank.take, args=(bk,))

th1.start()
th2.start()

th1.join()
th2.join()

set_list = bk.str_balance
for j in set_list:
    print(j)

print(f'Итоговый баланс: \033[32m{bk.balance}\033[0m')
print()
print(thanks)
