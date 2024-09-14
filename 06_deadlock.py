import threading
import time


lock1 = threading.Lock()
lock2 = threading.Lock()


def thread_task1():
    with lock1:
        print("Thread 1 acquired lock 1")
        time.sleep(0.05)

        with lock2:
            print("Thread 1 acquired lock 2")

def thread_task2():
    with lock2:
        print("Thread 2 acquired lock 2")
        time.sleep(0.05)

        with lock1:
            print("Thread 2 acquired lock 1")

def main():
    thread1 = threading.Thread(target=thread_task1)
    thread2 = threading.Thread(target=thread_task2)

    thread1.start()
    thread2.start()

    thread1.join()
    thread2.join()

    print("finished")

# данная программа печатает
# Thread 1 acquired lock 1
# Thread 2 acquired lock 2
# Происходит это потому что Поток 1 получает Лок 1 и ожидает освобождения лока 2
# в свою очередь, Поток 2 получает Лок 2 и ожидает освобождения Лока 1, чего никогда не происходит.
# Один из способов исправить это -- установить одинаковую последовательность получения Потоками Локов
# (например, сначала 1, затем 2).

def thread_task1_fixed():
    with lock1:
        print("Thread 1 acquired lock 1")
        time.sleep(0.05)

        with lock2:
            print("Thread 1 acquired lock 2")

def thread_task2_fixed():
    with lock1:
        print("Thread 2 acquired lock 1")
        time.sleep(0.05)

        with lock2:
            print("Thread 2 acquired lock 2")

def main_fixed():
    thread1_fixed = threading.Thread(target=thread_task1_fixed)
    thread2_fixed = threading.Thread(target=thread_task2_fixed)

    thread1_fixed.start()
    thread2_fixed.start()

    thread1_fixed.join()
    thread2_fixed.join()

    print("finished")


if __name__ == "__main__":
    main_fixed()

# Исправленная программа печатает
# Thread 1 acquired lock 1
# Thread 1 acquired lock 2
# Thread 2 acquired lock 1
# Thread 2 acquired lock 2
