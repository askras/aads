import random
import timeit
import functools
import matplotlib.pyplot as plt

def radix_sort(arr):
    max_num = max(arr)
    exp = 1

    while max_num // exp > 0:
        counting_sort(arr, exp)
        exp *= 10

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

    for i in range(n):
        arr[i] = output[i]

def shaker_sort(arr):
    n = len(arr)
    swapped = True
    start = 0
    end = n - 1

    while (swapped and start < end):
        swapped = False
        for i in range(start, end):
            if (arr[i] > arr[i + 1]):
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                swapped = True

        if not swapped:
            break

        swapped = False
        end -= 1
        for i in range(end - 1, start - 1, -1):
            if (arr[i] > arr[i + 1]):
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                swapped = True
        start += 1

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

def test_sorting_algorithms(sort_function, array_type, array_size=10):
    sorted_array = list(range(array_size))
    reversed_array = list(range(array_size, 0, -1))
    random_array = random.sample(range(array_size * 10), array_size)

    arrays = {'sorted': sorted_array, 'reversed': reversed_array, 'random': random_array}

    for array_name, array in arrays.items():
        print(f"{array_type} array ({array_name}): {array}")
        for i in range(3):
            array_copy = array.copy()
            start_time = timeit.default_timer()
            sort_function(array_copy)
            elapsed_time = timeit.default_timer() - start_time
            print(f"Run {i + 1}: {sort_function.__name__} took {elapsed_time:.6f} seconds. Sorted array: {array_copy}")
        print("\n")

print("Radix Sort:")
test_sorting_algorithms(radix_sort, "Radix Sort")

print("Shaker Sort:")
test_sorting_algorithms(shaker_sort, "Shaker Sort")







# Подготовка массивов:
#
# sorted_array: Массив, упорядоченный по возрастанию.
# reversed_array: Массив, упорядоченный по убыванию.
# random_array: Массив с случайным порядком элементов.
# Цикл по массивам:
#
# Для каждого типа массива (упорядоченного, упорядоченного в обратном порядке и случайного) выполняются следующие действия:
# Цикл тестирования:
#
# Внутренний цикл (3 повторения) тестирует сортировку на текущем массиве.
# Создается копия массива, чтобы избежать изменения оригинального массива.
# Измеряется время выполнения сортировки для данной копии.
# Результат теста выводится, включая затраченное время и отсортированный массив.
# Вывод результатов:
#
# Для каждого типа массива выводится информация о процессе сортировки (упорядоченный, упорядоченный в обратном порядке, случайный) и результаты теста для каждого запуска.