---
jupyter:
  jupytext:
    text_representation:
      extension: .md
      format_name: markdown
      format_version: '1.3'
      jupytext_version: 1.15.2
  kernelspec:
    display_name: Python 3 (ipykernel)
    language: python
    name: python3
---

# Шпаргалка по Python и Jupyter


## Загрузка кода из файла

```python
%load -r 16:19 vector.py
```

```python
%load -s Vector vector.py
```

## Сохранение кода в файл

```python
%%writefile class_info.py

import inspect

def get_class_info(cls):
    '''Displays information about the class'''

    print(f'Класс {cls.__name__}: # {cls.__doc__}')

    print('Attributes:')
    init_signature = inspect.signature(cls.__init__)
    for param_name, param in init_signature.parameters.items():
        if param.name != 'self':
            param_annotation = ': ' + str(param.annotation)[:-1]
            param_default = '' if str(param.default) == "<class 'inspect._empty'>" else ' = ' + str(param.default)
            print(f'    {param.name}{param_annotation}{param_default}')

    print('Methods:')
    for attribute in dir(cls):
        if callable(method:=getattr(cls, attribute)) and not attribute.startswith("__"):
            method_name = method.__name__
            method_args = inspect.signature(method)
            method_doc = str(inspect.getdoc(method)).splitlines()[0]
            print(f'    {method_name}{method_args}: # {method_doc}')
```

```python
# %load class_info.py

import inspect

def get_class_info(cls):
    '''Displays information about the class'''

    print(f'Класс {cls.__name__}: # {cls.__doc__}')

    print('Attributes:')
    init_signature = inspect.signature(cls.__init__)
    for param_name, param in init_signature.parameters.items():
        if param.name != 'self':
            param_annotation = ': ' + str(param.annotation)[:-1]
            param_default = '' if str(param.default) == "<class 'inspect._empty'>" else ' = ' + str(param.default)
            print(f'    {param.name}{param_annotation}{param_default}')

    print('Methods:')
    for attribute in dir(cls):
        if callable(method:=getattr(cls, attribute)) and not attribute.startswith("__"):
            method_name = method.__name__
            method_args = inspect.signature(method)
            method_doc = str(inspect.getdoc(method)).splitlines()[0]
            print(f'    {method_name}{method_args}: # {method_doc}')

```

```python
get_class_info(Vector)
```

```python
from class_info import get_class_info

get_class_info(Vector)
```

## Дополнение кода в файле

```python
%%writefile vector_info.py
import vector
```

```python
%%writefile -a vector_info.py
import class_info
```

```python
%%writefile -a vector_info.py
class_info.get_class_info(vector.Vector)
```

## Запуск кода из файла

```python
%run vector_info.py
```

## Вызов справки

```python
help(len)
```

```python
len.__doc__
```

```python
# Справка по собственному коду
help(Vector.norm)
```


```python
%lsmagic
```

```python
%load?
```

```python
len?
```

```python
Vector.radius?
```

## Работа с терминалом

```python
!ls
```

```bash
echo Hello World!
```

### pydoc

```bash

python -m pydoc vector
```

```python
!python -m pydoc vector
```

```bash

python -m pydoc -n localhost
```

```python
!python -m pydoc -w vector
```

```python
!python -m pydoc -w vector.Vector.norm
```

### doctest

```bash
python -m doctest vector.py
```

## Куда еще посмотреть?

```python
dir(str)
```

```python
import random

random.__dir__()
```

```python
dir(Vector)
```



## Оформление кода

1. https://github.com/google/styleguide/blob/gh-pages/pyguide.md#38-comments-and-docstrings

2. https://numpydoc.readthedocs.io/en/latest/format.html



1. Переменныи, функции - snake_case
2. Классы - CamelCase
3. docstring


### Именование

1. _bar - private
2. __ init __ - builts !!! НЕ ИСПОЛЬЗОВАТЬ
3. class_
4. __var - защитное переименование


### Принципы
1. Принцип одной ответственности
2. Принцип наименьшего удивления
3. Комментарии врут
4. TDD
5. Типизация (+/-)
6. Будь консервативен, когда передаешь, будь либерален, когда принимаешь. (Закон Постела, или принцип надежности)
7. Преждевременная оптимизация вредна
8. ....


## Полезые инструменты
1. Линтеры: flake8, pylint
2. Инструменты форматирования: autopep, black, blue
3. Проверка типов: mypy, pytype
4. Тестирование: pytest, unittest


## Не делайте так :) 
СМС-код или Twitter-код


### Колода карт

```python
suits = 'spades diamonds clubs hearts'.split()
suits = ['spades', 'diamonds', 'clubs', 'hearts']
```

```python
ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
print(ranks)
ranks = list(map(lambda _: '10' if _=='x' else _, '23456789xJQKA'))
print(ranks)
ranks = list(map(lambda _: _.replace('x', '10'), '23456789xJQKA'))
print(ranks)
ranks = ['10' if _=='x' else _ for _ in '23456789xJQKA']
print(ranks)
ranks = [_.replace('x', '10') for _ in '23456789xJQKA']
print(ranks)
ranks = [str(_) for _ in range(2, 11)] + list('JQKA')
print(ranks)
ranks = list('23456789') + ['10'] + list('JQKA')
print(ranks)
ranks = '2 3 4 5 6 7 8 9 10 J Q K A'.split()
print(ranks)
ranks = list('23456789JQKA') + ['10']
print(ranks)так
```

```python
ranks = ['6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
print(ranks)
ranks = list(map(lambda _: '10' if _=='x' else _, '6789xJQKA'))
print(ranks)
ranks = list(map(lambda _: _.replace('x', '10'), '6789xJQKA'))
print(ranks)
ranks = ['10' if _=='x' else _ for _ in '6789xJQKA']
print(ranks)
ranks = [_.replace('x', '10') for _ in '6789xJQKA']
print(ranks)
ranks = [str(_) for _ in range(6, 11)] + list('JQKA')
print(ranks)
ranks = list('6789') + ['10'] + list('JQKA')
print(ranks)
ranks = '6 7 8 9 10 J Q K A'.split()
print(ranks)
ranks = list('6789JQKA') + ['10']
print(ranks)
```

### Угадайка 1

```python
def f(d,m,y):return(d:=d%(((3,y%4-1<0<y%25|(y%16<1))+2*(3,2,3,2,3))[m-1]+28)+1,m:=(m+(d<2))%12,y+(d*m<2))
f=lambda d,m,y:(d:=d%(((3,y%4-1<0<y%25|(y%16<1))+2*(3,2,3,2,3))[m-1]+28)+1,m:=(m+(d<2))%12,y+(d*m<2))

```

```python

```

```python
def f(d,m,y):return(d:=d%(((3,y%4-1<0<y%25|(y%16<1))+2*(3,2,3,2,3))[m-1]+28)+1,m:=(m+(d<2))%12,y+(d*m<2))

assert f(31, 12, 12) == (1, 1, 13)
assert f(1, 1, 1) == (2, 1, 1)
assert f(28, 2, 16) == (29, 2, 16)
assert f(31, 8, 2022) == (1, 9, 2022)
assert f(28, 2, 1200) == (29, 2, 1200)
assert f(28, 2, 1201) == (1, 3, 1201)
assert f(28,2,2000) == (29, 2, 2000)
assert f(28,2,1900) == (1, 3, 1900)
assert f(20,10,2023) == (21,10,2023)
```

```python
f=lambda d,m,y:(d:=d%(((3,y%4-1<0<y%25|(y%16<1))+2*(3,2,3,2,3))[m-1]+28)+1,m:=(m+(d<2))%12,y+(d*m<2))

assert f(31, 12, 12) == (1, 1, 13)
assert f(1, 1, 1) == (2, 1, 1)
assert f(28, 2, 16) == (29, 2, 16)
assert f(31, 8, 2022) == (1, 9, 2022)
assert f(28, 2, 1200) == (29, 2, 1200)
assert f(28, 2, 1201) == (1, 3, 1201)
assert f(28,2,2000) == (29, 2, 2000)
assert f(28,2,1900) == (1, 3, 1900)
assert f(20,10,2023) == (21,10,2023)
```

```python
def next_data(current_day, current_month, current_year):
    '''Вычисление даты следующего дня'''
    
    # Количество дней в феврале
    if (current_year % 4 == 0 and current_year % 100 != 0) or (current_year % 400 == 0):
        DAYS_IN_FEBRUARY = 29
    else:
        DAYS_IN_FEBRUARY = 28
    
    # Количество дней по месяцам (0 в начале, чтобы счет шел с 1)
    DAYS_IN_MONTH = (31,DAYS_IN_FEBRUARY,31,30,31,30,31,31,30,31,30,31)
    
    # Вычисление следующего дня
    next_day = current_day % DAYS_IN_MONTH[current_month - 1] + 1
    
    # Вычисление следующего месяца
    if next_day == 1:
        next_month = (current_month + 1) % 12
    else:
        next_month = current_month
    
    # Вычисление следующего года
    if next_day == 1 and next_month == 1:
        next_year = current_year + 1
    else: 
        next_year = current_year
    
    return next_day, next_month, next_year


assert next_data(31, 12, 12) == (1, 1, 13)
assert next_data(1, 1, 1) == (2, 1, 1)
assert next_data(28, 2, 16) == (29, 2, 16)
assert next_data(31, 8, 2022) == (1, 9, 2022)
assert next_data(28, 2, 1200) == (29, 2, 1200)
assert next_data(28, 2, 1201) == (1, 3, 1201)
assert next_data(28,2,2000) == (29, 2, 2000)
assert next_data(28,2,1900) == (1, 3, 1900)
assert next_data(20,10,2023) == (21,10,2023)
```

```python
def next_data(current_day, current_month, current_year):
    
    if (current_year % 4 == 0 and current_year % 100 != 0) or (current_year % 400 == 0):
        DAYS_IN_FEBRUARY = 29
    else:
        DAYS_IN_FEBRUARY = 28
    
    DAYS_IN_MONTH = (31,DAYS_IN_FEBRUARY,31,30,31,30,31,31,30,31,30,31)
    
    next_day = current_day % DAYS_IN_MONTH[current_month - 1] + 1
    
    if next_day == 1:
        next_month = (current_month + 1) % 12
    else:
        next_month = current_month
    
    if next_day == 1 and next_month == 1:
        next_year = current_year + 1
    else: 
        next_year = current_year
    
    return next_day, next_month, next_year


assert next_data(31, 12, 12) == (1, 1, 13)
assert next_data(1, 1, 1) == (2, 1, 1)
assert next_data(28, 2, 16) == (29, 2, 16)
assert next_data(31, 8, 2022) == (1, 9, 2022)
assert next_data(28, 2, 1200) == (29, 2, 1200)
assert next_data(28, 2, 1201) == (1, 3, 1201)
assert next_data(28,2,2000) == (29, 2, 2000)
assert next_data(28,2,1900) == (1, 3, 1900)
assert next_data(20,10,2023) == (21,10,2023)
```

### Угадайка 2

```python
q = lambda l: q([x for x in l[1:] if x <= l[0]]) + [l[0]] + q([x for x in l if x > l[0]]) if l else []
```

### Угадайка 3

```python
a = b - a
b = b - a
a = b + a
```
