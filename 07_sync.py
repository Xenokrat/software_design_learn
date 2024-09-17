## 1. Events
def event_example():
    import threading
    import time

    event = threading.Event()

    def waiter():
        print("Ожидаем, пока другой поток не уведомит нас...")
        event.wait()
        print("Уведомление получено, продолжаем...")

    def setter():
        time.sleep(2)
        print("Производим событие.")
        event.set()

    waiter_thread = threading.Thread(target=waiter)
    setter_thread = threading.Thread(target=setter)

    waiter_thread.start()
    setter_thread.start()

    waiter_thread.join()
    setter_thread.join()

## 2. Events аналогичный пример для AsyncIO
def aio_event_example():
    import asyncio

    event = asyncio.Event()

    async def waiter():
        print("Ожидаем, пока другой поток не уведомит нас...")
        await event.wait()
        print("Уведомление получено, продолжаем...")

    async def setter():
        await asyncio.sleep(2)
        print("Производим событие.")
        event.set()

    async def main():
        await asyncio.gather(waiter(), setter())

    asyncio.run(main())


## 3. Использование Барьеров
def barrier_example():
    import threading
    import time
    import random

    # Создаём барьеры для трех потоков
    barrier = threading.Barrier(3)

    def worker(thread_id):
        print(f"Тред {thread_id} подготовка...")
        time.sleep(random.randint(1, 5))

        # Все потоки должны "дождаться" в этом месте у барьера
        print(f"Тред {thread_id} ожидает...")
        barrier.wait()

        # Эта часть кода продолжит работать, когда все потоки
        # закончат работу
        print(f"Тред {thread_id} продолжает работу...")

    # Создаём и запускает 3 протока
    threads = [threading.Thread(target=worker) for _ in range(3)]

    for thread in threads:
        thread.start()

    # Окончание работы потоков
    for thread in threads:
        thread.join()

    print("Все треды дошли до барьера, синхронизировались и продолжили работу до конца")


# 4. Фьючерсы
def futures_example():
    # ThreadPoolExecutor: создаёт пул потоков (3 шт.)
    # Submitting Tasks: метод submit отправляет задачу в пул тредов, и возвращает Фючерс, который представляет собой результат отложенного вычисления
    # Collecting Results: as_completed(futures) метод возвращает итератор, который получает значения из фьючерсов по завершению работы (с future.result())
    from concurrent.futures import ThreadPoolExecutor, as_completed
    import time

    def worker(task_id):
        print(f"Задача {task_id} стартует...")
        time.sleep(2)  # Симуляция работы
        print(f"Задача {task_id} завершена.")
        return f"Результат задачи {task_id}"

    # ThreadPoolExecutor контекстный менеджер очистит всё что связано с созданием тредов в конце
    with ThreadPoolExecutor(max_workers=3) as executor:
        # Создаём фьючерсы, отправляя "работу" экзекьютору
        futures = [executor.submit(worker, i) for i in range(5)]

        # Получаем результат по завершению всей работы
        for future in as_completed(futures):
            result = future.result()
            print(result)

    print("Все задачи завершены")


# 5. Локи
def locks_example():
    import threading
    import time

    # Общий счётчик
    counter = 0

    counter_lock = threading.Lock()

    def increment_counter(thread_id):
        global counter
        for _ in range(1000):
            # Устанавливается лок перед работой с значением
            with counter_lock:
                temp = counter
                # симулируем работу в треде
                time.sleep(0.0001)
                counter = temp + 1

        print(f"Тред {thread_id} завершён")

    # Создание тредов
    threads = [threading.Thread(target=increment_counter, args=(i,)) for i in range(5)]

    # Запуск работы тредов
    for thread in threads:
        thread.start()

    # Завершение работы всех тредов
    for thread in threads:
        thread.join()

    print(f"Общий счётчик: {counter}")
