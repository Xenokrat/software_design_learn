"""
public class ThreadExample {
    private static int counter = 0;

    public static void main(String[] args) {
        Runnable task = () -> {
            for (int i = 0; i < 1000; i++) {
                counter++;
            }
        };

        Thread thread1 = new Thread(task);
        Thread thread2 = new Thread(task);

        thread1.start();
        thread2.start();

        try {
            thread1.join();
            thread2.join();
        } catch (InterruptedException e) {
            e.printStackTrace();
        }

        System.out.println("Counter: " + counter);
    }
}
"""

import multiprocessing

# Пофиксим код, используя Lock

counter = multiprocessing.Value('i', 0)

def thread_example(lock) -> None:
    for _ in range(1000):
        lock.acquire()
        temp = counter.value
        temp += 1
        counter.value = temp
        lock.release()

def main() -> None:
    lock = multiprocessing.Lock()

    process1 = multiprocessing.Process(target=thread_example, args=(lock,))
    process2 = multiprocessing.Process(target=thread_example, args=(lock,))

    process1.start()
    process2.start()

    try:
        process1.join()
        process2.join()
    except Exception as e:
        print(e)

    print(f"Counter {counter.value}")


if __name__ == "__main__":
    main()
