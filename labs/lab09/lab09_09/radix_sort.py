import random
import timeit
import functools
import matplotlib.pyplot as plt

def radix_sort(arr):
    def counting_sort(arr, exp):
        n = len(arr)
        output = [0] * n
        count = [0] * 10

        for i in range(n):
            index = arr[i] // exp
            count[index % 10] += 1

        for i in range(1, 10):
            count[i] += count[i - 1]

        i = n - 1
        while i >= 0:
            index = arr[i] // exp
            output[count[index % 10] - 1] = arr[i]
            count[index % 10] -= 1
            i -= 1

        i = 0
        for i in range(n):
            arr[i] = output[i]

    max_num = max(arr)
    exp = 1
    while max_num // exp > 0:
        counting_sort(arr, exp)
        exp *= 10

@functools.lru_cache(maxsize=None)
def timing_decorator(ndigits: int, number: int) -> callable:
    def decorator(func: callable) -> callable:
        @functools.wraps(func)
        def wrapper(*args, **kwargs) -> float:
            usage_time = timeit.timeit(
                lambda: func(*args, **kwargs),
                number=number,
            )
            return round(usage_time / number, ndigits)

        return wrapper

    return decorator

max_n = 100001
max_vector = [random.randint(1, 100) for _ in range(max_n)]

ndigits = 6
number_of_runs = 5

n_values = [1000, 5000, 10000, 100000]
average_times_radix_sort = []

@timing_decorator(ndigits, number_of_runs)
def calculate_radix_sort(vector):
    radix_sort(vector)

for n in n_values:
    print(n)

    average_time = calculate_radix_sort(max_vector[:n])
    average_times_radix_sort.append(average_time)

plt.plot(n_values, average_times_radix_sort, linestyle='-', color='b')
plt.title('Зависимость времени поразрядной сортировки от n')
plt.xlabel('n')
plt.ylabel('Среднее время выполнения (секунды)')

plt.savefig('radix_sort_time_.png')
