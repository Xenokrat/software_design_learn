import multiprocessing

counter = multiprocessing.Value('i', 0)

# Интересно, что треды в Python дают всегда правильный результат,
# даже без локов, видимо из-за GIL. Поэтому в данном случае для
# наглядности использую multiprocessing, суть идеи от этого, думаю, не изменяется

# Ошибка получается из-за того, что несколько процессов одновременно
# пытаются получить доступ к значению, поэтому часть работы может потеряться и 
# итоговое значение будет меньше, чем нужно

def increment_counter_incorrect(counter):
    for _ in range(100000):
        temp = counter.value
        temp += 1
        counter.value = temp

def main_incorrect():
    number_of_processes = 10
    processes = []

    for _ in range(number_of_processes):
        process = multiprocessing.Process(target=increment_counter_incorrect, args=(counter,))
        processes.append(process)
        process.start()

    for process in processes:
        process.join()

    print(f"Final counter value: {counter.value}")

# в исправленной версии мы использует Локи, которые позволяют 
# сделать операции атомарными. Поэтому когда один поток изменяет
# значение счётчика, другие потоки вынуждены ожидать доступа

def increment_counter_correct(counter, lock):
    for _ in range(100000):
        with lock:
            temp = counter.value
            temp += 1
            counter.value = temp

def main_correct():
    number_of_processes = 10
    processes = []
    lock = multiprocessing.Lock()

    for _ in range(number_of_processes):
        process = multiprocessing.Process(target=increment_counter_correct, args=(counter, lock))

        processes.append(process)
        process.start()

    for process in processes:
        process.join()

    print(f"Final counter value: {counter.value}")


if __name__ == "__main__":
    main_correct()