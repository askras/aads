import functools
import timeit
import typing
import matplotlib.pyplot as plt
import random
import numpy as np

def get_usage_time(
    *, number: int = 1, setup: str = 'pass', ndigits: int = 3
) -> typing.Callable:
    """Decorator for measuring the speed of the function (in seconds)

    Parameters
    ----------
    number : int, optional
        Number of code repetitions.
    setup : str, optional
        Code executed once before timing.
    ndigits : int, optional
        Number of decimal places in the returned value.

    Returns
    -------
    decorator: typing.Callable
        Decorator for measuring the time of the function in seconds.

    See Also
    --------
    timeit
        Measure execution time of small code snippets.

    References
    ----------
    [1] timeit documentation : https://docs.python.org/3/library/timeit.html

    Examples
    --------
    Decorating an existing function:

    >>> import time
    >>> def sleep_func(n):
    ...     time.sleep(n)
    ...     return n
    ...
    >>> get_usage_time_sleep_func = get_usage_time()(sleep_func)
    >>> time_sleep_func = get_usage_time_sleep_func(2)
    >>> print(f'The function was executed for {time_sleep_func} seconds')
    The function was executed for 2.0 seconds
    >>> get_usage_time(number=5)(sleep_func)(4)
    4.0

    Measuring the running time of a function for different parameter values:

    >>> import time
    >>> def sleep_func(n):
    ...     time.sleep(n)
    ...     return n
    ...
    >>> for n in range(1,4):
    ...    get_usage_time_sleep_func = get_usage_time(number=2)(sleep_func)
    ...    print(get_usage_time_sleep_func(n))
    1.0
    2.0
    3.0

    Using the `setup` option:

    >>> import time
    >>> def sleep_func(n):
    ...     time.sleep(n)
    ...     return n
    ...
    >>> setup = 'print("Start setup"); time.sleep(10); print("End setup")'
    >>> get_usage_time_sleep_func = get_usage_time(setup=setup)(sleep_func)
    >>> print(get_usage_time_sleep_func(3))
    Start setup
    End setup
    3.0

    Decoding the generated function:

    >>> import time
    >>> @get_usage_time(number=2, setup='print("Start");', ndigits=0)
    ... def sleep_func(n):
    ...    time.sleep(n)
    ...    return n
    ...
    >>> time_sleep_func = sleep_func(3)
    Start
    >>> print(time_sleep_func)
    3.0
    """

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

N = 20 - 16
n = N*(10**5)
x = 1.5*N
step = 100*N
vec = [random.randint(1, 1000) for _ in range(n)]
name_vec = ['1.1 Constant function', '1.3 The product of the elements', '1.4 Calculation of the polynomial by the Gorner method', '1.5 Searching for the maximum by simple brute force', '1.7 Arithmetic mean', '2 Matrix multiplication']
A = np.array([[random.randint(1, 1000) for _ in range(n//400)] for _ in range(n//400)])
B = np.array([[random.randint(1, 1000) for _ in range(n//400)] for _ in range(n//400)])

def creater_grafs(func, name, matrix) :
    if matrix:
        items = [i for i in range(1, n//400, step//10)]
        times = [func(A[:i, :i], B[:i, :i]) for i in items]
    else:
        items = [i for i in range(1, n, step)]
        times = [func(vec[:i]) for i in items]    
    fig = plt.plot(items, times, 'bo-')
    plt.title(name)
    ax = plt.gca()
    ax.set_xlabel('Number of elements, $n$ ')
    ax.set_ylabel('Time, sec')
    plt.savefig(name + '.png')
def f1(v) :
    return N
def f3(v) :
    res = 1
    for k in v:
        res *= k
    return res
def f4(v) :
    res = 0
    for k in v[::-1]:
        res += k +res*x
    return res
def f5(v) :
    res = 0
    for k in v:
        if k > res :
            res = k
    return res
def f7(v) :
    res = 0
    for k in v:
        res += k
    return res/len(v)
def matrix_multiplication(A, B) :
    return np.dot(A, B)
    
func = get_usage_time(number=5, ndigits=5)(matrix_multiplication)
creater_grafs(func, name_vec[5], 1)
            
