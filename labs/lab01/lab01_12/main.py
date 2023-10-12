import numpy as np
import functools
import timeit
import typing
import random
import matplotlib.pyplot as plt


def get_usage_time(
        *, number: int = 5, setup: str = 'pass', ndigits: int = 3
) -> typing.Callable:
    def decorator(func: typing.Callable) -> typing.Callable:
        @functools.wraps(func)
        def wrapper(*args, **kwargs) -> float:
            usage_time = timeit.timeit(
                lambda: func(*args, **kwargs),
                setup=setup,
                number=number,
            )
            return round(usage_time / number, ndigits)

        return wrapper

    return decorator


def sum_vector(n):
    return sum(vector[:n])


def max_by_bubble(n):
    number = 0
    for i in range(1, n):
        if number < vector[i]:
            number = vector[i]
    return number


def average(n):
    return sum(vector[:n]) / len(vector[:n])


def harmonic(n):
    return len(vector[:n] / sum(1 / vector[:n]))


def matrix_multiplication(n):
    matrix1 = np.random.randint(1, 11, size=(n, n))
    matrix2 = np.random.randint(1, 11, size=(n, n))
    return matrix1[:n].dot(matrix2[:n])


"""func = get_usage_time(ndigits=5)(max_by_bubble)
for i in range(1, 800001, 800):
    print(f'The function was executed for {func(i)} seconds at n={i}.')"""

vector = []
vector = np.random.randint(1, 101, 800001)

func = get_usage_time(ndigits=5)(matrix_multiplication)

#items = range(1, 800001, 800)
items = range(1, 1001, 10)  # for matrix
times = [func(i) for i in items]

fig = plt.plot(items, times, 'g-')
plt.title('Matrix multiplication')
ax = plt.gca()
ax.set_xlabel('Number of elements in rows/columns')
ax.set_ylabel('Time, sec')
"""plt.show()"""

plt.savefig('PhotoToad_2.png')
