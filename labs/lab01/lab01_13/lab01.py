import functools
import random
import timeit
import typing
import matplotlib.pyplot as plt

%matplotlib inline

vec = [random.randint(1, 1000) for _ in range(0, 13 * 10 ** 5 + 1, 700)]


def get_usage_time(
        *, number: int = 1, setup: str = 'pass', ndigits: int = 3
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


def task1(vec: list[int]) -> int:
    return 7


def task2(vec:list[int], x=1.5*7):
    result = vec[-1]

    for i in range(len(vec) - 2, -1, -1):
        result = result * x + vec[i]

    return result

def task3(vec: list[int])->int:
    min = vec[0]
    for num in vec:
        if num < min:
            min = num
    return min

def task4(vec: list[int]):
    return sum(vec) / len(vec)

func = get_usage_time(ndigits=5)(task2)

print(func(vec))
