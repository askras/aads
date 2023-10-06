import random
import typing
import timeit
import functools
import matplotlib.pyplot as plt
import numpy as np


def timing_decorator(ndigits: int, number: int, setup: str) -> typing.Callable:
    def decorator(func: typing.Callable) -> typing.Callable:
        @functools.wraps(func)
        def wrapper(*args, **kwargs) -> float:
            usage_time = timeit.timeit(
                lambda: func(*args, **kwargs),
                globals=globals(),
                setup=setup,
                number=number,
            )
            return round(usage_time / number, ndigits)

        return wrapper

    return decorator


max_n = 1300000
max_vector = np.array([random.randint(1, 100) for _ in range(max_n)])

n_values = list(range(1, max_n, 1300))
average_times = []


@timing_decorator(6, 5, "import numpy as np")
def post_f(vector):
    harmonic_mean = 0.0
    for k in range(1, len(vector) + 1):
        harmonic_mean += 1 / vector[k - 1]
    harmonic_mean = len(vector) / harmonic_mean
    return harmonic_mean


for n in n_values:
    print(n)
    average_time = post_f(max_vector[:n])
    average_times.append(average_time)

plt.plot(n_values, average_times, linestyle='-', color='b')

plt.title('Зависимость среднего времени выполнения от n \n (от среднего гармонического)')
plt.xlabel('n')
plt.ylabel('Среднее время выполнения (секунды)')
plt.savefig('graph1.8.png')
