"""
Создайте функцию в демоне потока которая каждые 3 секунды будет писать "Вводите быстрее".
В основной части программы запросите ввод кода от бомбы и если код неверный выведите: "Вы взорвались", если верный - "Бомба разминирована"
"""
import threading
import time

def reminder_thread():
    while True:
        print("Type faster")
        time.sleep(3)

reminder_thread = threading.Thread(target=reminder_thread, daemon=True)

reminder_thread.start()

try:
    bomb_code = input("Enter code from bomb: ")
    if bomb_code == "12345":
        print("Bomb has been defused.")
    else:
        print("You are exploded :c")
except KeyboardInterrupt:
    print("Program was ended by user.")