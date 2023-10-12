import random
import typing
import timeit
import functools
import matplotlib.pyplot as plt
import numpy as np


def timing_decorator(ndigits: int, number: int) -> typing.Callable:
    def decorator(func: typing.Callable) -> typing.Callable:
        @functools.wraps(func)
        def wrapper(*args, **kwargs) -> float:
            usage_time = timeit.timeit(
                lambda: func(*args, **kwargs),
                number=number,
            )
            return round(usage_time / number, ndigits)

        return wrapper

    return decorator


max_n = 1001

ndigits = 6
number_of_runs = 5

n_values = list(range(1, max_n, 8))
average_times = []


@timing_decorator(ndigits, number_of_runs)
def matrix_multiply(matrix_A, matrix_B):
    return np.dot(matrix_A, matrix_B)


for n in n_values:
    print(n)

    matrix_A = np.random.randint(1, 100, size=(n, n))
    matrix_B = np.random.randint(1, 100, size=(n, n))

    average_time = matrix_multiply(matrix_A, matrix_B)
    average_times.append(average_time)

plt.plot(n_values, average_times, linestyle='-', color='b')
plt.title('Зависимость времени выполнения матричного умножения от n')
plt.xlabel('порядок матриц - n')
plt.ylabel('Среднее время выполнения (секунды)')
plt.savefig('matrix.png')