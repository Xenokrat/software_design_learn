"""
import java.util.Random;

public class ComplexMultiThreadProcessing {
    private static final int SIZE = 1000000;
    private static final int THREADS = 4;
    private static final int[] data = new int[SIZE];
    private static volatile int sum = 0;

    public static void main(String[] args) {
        Random random = new Random();
        for (int i = 0; i < SIZE; i++) {
            data[i] = random.nextInt(100);
        }

        Thread[] threads = new Thread[THREADS];
        int chunkSize = SIZE / THREADS;

        for (int i = 0; i < THREADS; i++) {
            final int start = i * chunkSize;
            final int end = (i + 1) * chunkSize;
            threads[i] = new Thread(() -> {
                int localSum = 0;
                for (int j = start; j < end; j++) {
                    localSum += data[j];
                }
                synchronized (ComplexMultiThreadProcessing.class) {
                    sum += localSum;
                }
            });
            threads[i].start();
        }

        for (int i = 0; i < THREADS; i++) {
            try {
                threads[i].join();
            } catch (InterruptedException e) {
                e.printStackTrace();
            }
        }

        System.out.println("Sum of all elements: " + sum);
    }
}
"""

import random
from concurrent.futures import ProcessPoolExecutor
# Используем ProcessPoolExecutor, который запускает multiprocessing под капотом
# Питоновские треды в данном случае не сработают из-за GIL

TESTING = True
SIZE: int = 1_000_000
THREADS: int = 4
# определяем размер чанка, т.к. он зависит только от констант
CHUNK_SIZE = SIZE // THREADS

def _sum_list(lst): return sum(lst)

def main() -> None:
    data = [random.randint(0, 100) for _ in range(SIZE)]

    # Запускаем пул процессов, с указанным количеством воркеров
    with ProcessPoolExecutor(max_workers=THREADS) as executor:
        # Делим лист на кусочки, которые могут обработать треды по чанкам
        chunks = [data[i:i + CHUNK_SIZE] for i in range(0, SIZE, CHUNK_SIZE)]
        # Мап распределит переданную работу по воркерам, чанки мы уже разбили выше
        # (заметка: lambda не сработает ниже, map нужна именованная функция как _sum_list)
        result = sum(executor.map(_sum_list, chunks))

    print(f"Sum of all elements: {result}")


if __name__ == "__main__":
    main()


