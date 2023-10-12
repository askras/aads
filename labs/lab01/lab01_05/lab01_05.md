---
jupyter:
  jupytext:
    text_representation:
      extension: .md
      format_name: markdown
      format_version: '1.3'
      jupytext_version: 1.15.1
  kernelspec:
    display_name: Python 3 (ipykernel)
    language: python
    name: python3
---

```python
import functools
import timeit
import typing
import random
import matplotlib.pyplot as plt
%matplotlib inline

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

def my_func(n):
    c=5
    return c

N=20-5
items = range(1, N*10**5, 100*N)
times=[]
func = get_usage_time(ndigits=5)(my_func)
for n in items:
    time=0
    for i in range(1,6):
        time=time+func(n)
    times.append(time/5)

fig = plt.plot(items, times, 'bo-')
plt.title('The execution time of the sorting algorithm')
ax = plt.gca()
ax.set_xlabel('Number of elements, $10^n$ pieces')
ax.set_ylabel('Time, sec')
plt.show()
```

```python
import functools
import timeit
import typing
import random
import matplotlib.pyplot as plt
%matplotlib inline

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

def my_func(n):
    L = [random.randint(1, 1000) for _ in range(n)]
    pro=1
    for c in range(1,len(L),100*(20-5)):
        pro=pro*L[c]
    return pro


N=20-5
items = range(1, N*10**5, 100*N)
times=[]
func = get_usage_time(ndigits=5)(my_func)
for n in items:
    time=0
    for i in range(1,6):
        time=time+func(n)
    times.append(time/5)
    
fig = plt.plot(items, times, 'bo-')
plt.title('The execution time of the sorting algorithm')
ax = plt.gca()
ax.set_xlabel('Number of elements, $10^n$ pieces')
ax.set_ylabel('Time, sec')
plt.show()
```

```python
import functools
import timeit
import typing
import random
import matplotlib.pyplot as plt
%matplotlib inline

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

def my_func(n):
    L = [random.randint(1, 1000) for _ in range(n)]
    min=L[0]
    for c in range(1,len(L),100*(20-5)):
        if min>L[c]: 
            min=L[c]
    return min

N=20-5
items = range(1, N*10**5, 100*N)
times=[]
func = get_usage_time(ndigits=5)(my_func)
for n in items:
    time=0
    for i in range(1,6):
        time=time+func(n)
    times.append(time/5)

fig = plt.plot(items, times, 'bo-')
plt.title('The execution time of the sorting algorithm')
ax = plt.gca()
ax.set_xlabel('Number of elements, $10^n$ pieces')
ax.set_ylabel('Time, sec')
plt.show()
```

```python
import functools 
import timeit 
import typing 
import random 
import matplotlib.pyplot as plt 
%matplotlib inline

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

def my_func(n): 
    L = [random.randint(1, 1000) for _ in range(n)] 
    suma=1
    kol=1
    srgarm=0
    for c in range(1,len(L),100*(20-5)): 
        suma=suma+1/L[c] 
        kol+=1
    if suma!=1:
        suma-=1
        kol-=1
    srgarm=kol/suma 
    return srgarm

N=20-5
items = range(1, N*10**5, 100*N) 
times=[] 
func = get_usage_time(ndigits=5)(my_func) 
for n in items:
    time=0 
    for i in range(1,6): 
        time=time+func(n) 
    times.append(time/5)

fig = plt.plot(items, times, 'bo-')
plt.title('The execution time of the sorting algorithm')
ax = plt.gca()
ax.set_xlabel('Number of elements, $10^n$ pieces')
ax.set_ylabel('Time, sec')
plt.show()
```

```python
import functools
import timeit
import typing
import random
import matplotlib.pyplot as plt
%matplotlib inline

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

def my_func(n):
    A=[[0 for a in range(0,n)]for b in range(0,n)]
    B=[[0 for a in range(0,n)]for b in range(0,n)]
    C=[[0 for a in range(0,n)]for b in range(0,n)]
    for i in range(0,n,100*(20-5)):
        for j in range(0,n,100*(20-5)):
            A[i][j]=random.randint(1, 10)
            B[i][j]=random.randint(1, 10)

    for i in range(0,n,100*(20-5)):
        for j in range(0,n,100*(20-5)):
            for k in range(0,n,100*(20-5)):
                C[i][j]+=A[i][k]*B[k][j]
    return C

N=20-5
items = range(1, N*10**3, 100*N)
times=[]
func = get_usage_time(ndigits=5)(my_func)
for n in items:
    time=0
    for i in range(1,6):
        time=time+func(n)
    times.append(time/5)

fig = plt.plot(items, times, 'bo-')
plt.title('The execution time of the sorting algorithm')
ax = plt.gca()
ax.set_xlabel('Number of elements, $10^n$ pieces')
ax.set_ylabel('Time, sec')
plt.show()
```

```python

```

```python

```
