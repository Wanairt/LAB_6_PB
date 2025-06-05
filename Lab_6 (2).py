import time
import math
import matplotlib.pyplot as plt

def f_recursive(n):
    if n == 1 or n == 2:
        return 1
    else:
        sign = 1 if n % 2 == 0 else -1
        return sign * (f_recursive(n-1) - math.factorial(n + 2))

def f_iterative(n):
    f = [0] * (n + 1)
    if n >= 1:
        f[1] = 1
    if n >= 2:
        f[2] = 1
    for i in range(3, n + 1):
        sign = 1 if i % 2 == 0 else -1
        f[i] = sign * (f[i - 1] - math.factorial(i + 2))
    return f[n]

if __name__ == '__main__':
    n_values = range(270, 301)  # Ограничение n для рекурсии
    recursive_times = []
    iterative_times = []

    for n in n_values:
        # Рекурсивное вычисление
        start_time = time.time()
        try:
            result_recursive = f_recursive(n)
            end_time = time.time()
            recursive_time = end_time - start_time
            recursive_times.append(recursive_time)
        except RecursionError:
            recursive_times.append(None)
            print(f"Рекурсия не работает для n = {n}")

        # Итеративное вычисление
        start_time = time.time()
        result_iterative = f_iterative(n)
        end_time = time.time()
        iterative_time = end_time - start_time
        iterative_times.append(iterative_time)

    # Таблица результатов
    print("n\tРекурсия (сек)\tИтерация (сек)")
    for i, n in enumerate(n_values):
        print(f"{n}\t{recursive_times[i]:.6f}\t\t{iterative_times[i]:.6f}")

    # График
    plt.plot(n_values, recursive_times, label='Рекурсия')
    plt.plot(n_values, iterative_times, label='Итерация')
    plt.xlabel('n')
    plt.ylabel('Время (сек)')
    plt.title('Сравнение времени вычисления')
    plt.legend()
    plt.grid(True)
    plt.show()