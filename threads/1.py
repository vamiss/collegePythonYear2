"""
Пример для демонстрации потоков, просто запустите и посмотрите как это работает
"""
import time
from threading import Thread

def sleepMe(i):
    print("Thread %i is sleeping during 5 secs.\n" % i)
    time.sleep(5)
    print("Thread %i is sleeping during 5 secs.\n" % i)
for i in range(10):
    th = Thread(target=sleepMe, args=(i, ))
    th.start()