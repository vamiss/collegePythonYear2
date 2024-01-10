"""
Создайте функцию напоминалку в отдельном потоке от основном программы.
Функция должна запрашивать о чем напомнить и через сколько секунд.
В основной части программы запустите поток с функцией и выполните задержку в 10 секунд.
После выполнения программа должна написать "программа завершается"
"""
import threading
import time

def reminder_thread():
    reminder_text = input("What type of alert? ")
    delay_seconds = int(input("Secs amount: "))

    time.sleep(delay_seconds)
    print(f"Alert: {reminder_text}")

reminder_thread = threading.Thread(target=reminder_thread)

reminder_thread.start()

try:
    time.sleep(10)
    print("Program is ending.")
except KeyboardInterrupt:
    print("Program was ended by user.)

reminder_thread.join()