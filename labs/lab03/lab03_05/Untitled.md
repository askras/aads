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

<!-- #region -->



# Отчет

## Лабораторная работа №2

### Линейный однонаправленный список

### Цель работы:

Изучение структуры данных «линейные двунаправленные списки», а также основных операций над ними.

### Задачи:

1. Реализовать программу, выполняющую стандартный набор операций с линейным двунаправленным списком:

- вставка элемента в начало списка;
- вставка элемента в середину списка перед указанным значением;
- вставка элемента в середину списка после указанного значения;
- вставка элемента в конец списка;
- удаление элемента в начале списка;
- Удаление элемента, стоящего перед указанным значением списка;
- Удаление элемента, стоящего после указанного значением списка;
- удаление определенного элемента в списке;
- удаление элемента в конце списка;
- очистка списка;
- поиск элемента списка по его значяению;
- реверс списка (переворачивание списка задом на перед).
- Требования:

2. Реализовать приложение, для работы со списком, которое реализует следующий набор действий:

а) инициализация пустого линейного однонаправленного списка;

б) организация диалогового цикла с пользователем;

3 Реализовать индивидуальное задание.

- Сформировать список целых чисел, вводимых пользователем, в том порядке, в котором вводятся эти числа, но без повторений элементов.
- Пусть имеется список L1 действительных чисел. Записать в список L2 все элементы списка L1, делящиеся на 3 в порядке убывания.

### Листинг программного кода с описанием

class Node:
    def __init__(self,data)

class LinkedList:
    def __init__(self)
        
    def push_front(self, data) # Добавляет элемент в начало списка
    
    def push_back(self,data) # Добавляет элемент в коней списка

    def push(self,index,data) # Добавляет элемент в указаное место в списке

    def push_before(self,value,data) # добавляет элемент перед значением
    
    def push_after(self,value,data) # добавляет элемент после значения
    
    def pop_front(self) # Удаляет первй элемент списка
    
    def pop_back(self) # Удаляет последний элемент списка

    def pop(self,index) # Удаляет указаный элемент списка

    def pop_before(self, value) # удаляет элемент перед значением

    def pop_after(self, value) # удаляет элемент после значения

    def pop_value(self,value) # удаляет элемент по значению

    def find_index(self,index) # Находит элемент по индексу

    def find_value(self, value) # ищет индекс элемента по значению
    
    def reverse(self) # Переворачивает список

    def print(self) # Выводит список

    def clear(self) # Очищает список

    def remove_dublicate(self) # удаляет все повторяющиеся элементы

    def sort_list(self) # Сортируют список

def merge_list(list1,list2) # Объединяет два списка и сортирует результирующий список, второй список отсортирован в обратном порядке  и состоит из чисел кратных 3

#Взаимодействие с пользователем

- while x!="start" # Просит ввести start пока пользователь его не введет

- while x!="stop" # программа работает пока пользователь не введет stop

    main() # печатает описание команд
  
    if x=="menu" # показывает меню команд
  
        while x!="end" # возвращает в главное меню
  
    if x=="list" # содержит операции работы над листом
  
        while x!="end" # возвращает в главное меню
  
            if x=="add" # содержит операции добавления элемента
  
                while x!="end" # возвращает в главное меню

                    if x=="begin" # добавляет элемент в начало
  
                        while x!="end" # возвращает в главное меню
                            
                    if x=="index" # добавляет элемент по индексу
  
                        while x!="end" # возвращает в главное меню

                    if x=="before" # добавляет элемент перед значением
  
                        while x!="end" # возвращает в главное меню 
  
                    if x=="after" # добавляет элемент после значения
  
                        while x!="end" # возвращает в главное меню 
      
                    if x=="tail" # добавляет элемент в конце
  
                        while x!="end" # возвращает в главное меню
    
            if x=="delete" # содержит команды удаления
  
                while x!="end" # возвращает в главное меню
  
                    if x=="begin" # удаляет в начале
  
                        while x!="end" # возвращает в главное меню
   
                    if x=="index" # удаляет по индексу
  
                        while x!="end" # возвращает в главное меню

                    if x=="value" # удаляет элемент по значению
  
                        while x!="end" # возвращает в главное меню 
  
                    if x=="before" # удаляет элемент перед значением
  
                        while x!="end" # возвращает в главное меню 
  
                    if x=="after" # удаляет элемент после значения
  
                        while x!="end" # возвращает в главное меню 
           
                    if x=="tail" # удаляет в конце
  
                        while x!="end" # возвращает в главное меню

            if x=="sort" # сортирует список
  
                while x!="end" # возвращает в главное меню

            if x=="clear" # очищает список
  
                while x!="end" # возвращает в главное меню

    if x=="find" # находит элемент в списке
  
        while x!="end" # возвращает в главное меню

            if x=="index" # находит элемент в списке по индексу
  
                while x!="end" # возвращает в главное меню

            if x=="value" # находит элемент в списке по значению
  
                while x!="end": # возвращает в главное меню   
 
    if x=="reverse" # переворачивает список
  
        while x!="end" # возвращает в главное меню
   
    f x=="remove dubl" # удаляет одинаковые элементы в списке
  
        while x!="end" # возвращает в главное меню

    if x=="merge" # объединяет и сортирует списки
  
        while x!="end" # возвращает в главное меню
   
    if x=="print" # печатает список
  
        while x!="end" # возвращает в главное меню

### Ответы на контрольные вопросы

1. Что такое динамическая структура данных?

Динамические структуры данных – это структуры данных, память под которые выделяется и освобождается программистом по мере необходимости. Динамические структуры данных в процессе существования в памяти могут изменять не только число составляю-щих их элементов, но и характер связей между элементами.

2. Что такое список?

Список — это упорядоченный набор элементов, каждый из которых имеет свой номер, или индекс, позволяющий быстро получить к нему доступ.

3. Какие виды списков существуют?

Списки бывают следующих видов:
- Маркированный. Перед элементом списка идет маркер.
- Нумерованный. Перед элементом списка идет номер.
- Список определений. Перед определением идет термин.
- Вложенный список.
- Многоуровневый. Список состоит из нескольких уровней. может быть маркированным. нумерованным и комбинированным.

4. Какие основные операции выполняются над списком?

Основными операциями над списками являются: 
· переход к очередному элементу списка; 
· добавление в список нового элемента; 
· поиск заданного элемента; 
· удаление элемента из списка. 
Выполнение этих операций основывается на использовании и изменении указателей. В отличие от очередей и стеков, элемент в список может быть добавлен в любое место.

5. Особенности выполнения операций вставки первого и не первого элемента.

Алгоритм вставки элемента: (после k-ого) первые k элементов остаются без изменений все элементы, начиная с k-ого сдвигаются на 1 позицию назад на место (k+1)-ого элемента записываем новый элемент. Массив из n элементов, в который вставляется k элементов необходимо определять как массив, имеющий размер n+k. Вставка перед элементом отличается только тем, что сдвигаются все элементы,

6. Особенности выполнения операций удаления первого и не первого элемента.

Если удаляется первый элемент в списке, то сначала переместить указатель начала списка на следующий элемент. Если в непустом списке удаляется не первый элемент (второй, третий и т.д., последний), то переместить указатель на позицию, следующую перед удаляемым элементом и  сместить указатель предыдущего элемента в обход удаляемого элемента


<!-- #endregion -->

```python

class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
        self.prev=None
        

class LinkedList:
    def __init__(self):
        self.head=None
        self.tail=None
        self.length=0
        
    def push_front(self, data):
        new_node=Node(data)
        if self.head is None:
            self.head=new_node
            self.tail=new_node
            self.head.prev=None
            self.tail.next=None
            
        else:
            self.head.prev=new_node
            new_node.next=self.head
            new_node.prev=None
            self.head=new_node
        self.length+=1
        return data
    
    def push_back(self,data):
        new_node=Node(data)
        if self.head is None:
            self.head=new_node
            self.tail=new_node
            self.head.prev=None
            self.tail.next=None
        else:
            self.tail.next=new_node
            new_node.prev=self.tail
            self.tail=new_node
            self.tail.next=None
        self.length+=1
        return data

    def push(self,index,data):
        index=int(index)
        if index<0:
            index+=self.length
        if index<0 or index>self.length:
            return "Index out of range"
        elif index==0:
            return self.push_front(data)
        elif index==self.length:
            return self.push_back(data)
        else:
            new_node=Node(data)
            current=self.head
            for _ in range(index-1):
                current=current.next
            new_node.next=current.next
            new_node.prev=current
            current.next.prev=new_node
            current.next=new_node
            self.length+=1
            return data
    
    def push_before(self,value,data):
        if self.head==None:
            return "error"
        index=self.find_value(value)
        if index=="Node is not present in the list":
            return "Node is not present in the list"
        item=self.push(str(index),data)
        return item

    def push_after(self,value,data):
        if self.head==None:
            return "error"
        index=self.find_value(value)
        if index=="Node is not present in the list":
            return "Node is not present in the list"
        item=self.push(str(index+1),data)
        return item
    
    def pop_front(self):
        if self.head is None:
            return "Insufficient data"
        old_head=self.head
        data=old_head.data
        if self.length==1:
            self.head=None
            self.tail=None
        else:
            self.head=old_head.next
            self.head.prev=None
        old_head=None
        self.length-=1
        return data
    
    def pop_back(self):
        if self.head is None:
            return "Insufficient data"
        data=self.tail.data
        old_head=self.tail
        if self.length==1:
            self.tail=None
            self.head=None
        else:
            self.tail=self.tail.prev
            self.tail.next=None
        old_head=None
        self.length-=1
        return data

    def pop(self,index):
        index=int(index)
        if index<0:
            index+=self.length
        if index<0 or index>=self.length:
            return "Index out of range"
        elif index==0:
            return self.pop_front()
        elif index==self.length-1:
            return self.pop_back()
        else:
            node=self.head
            for _ in range(index-1):
                node=node.next
            new_node=node.next
            node.next=new_node.next
            new_node.next.prev=node
            data=new_node.data
            new_node=None
            self.length-=1
            return data

    def pop_before(self, value):
        if self.head == None:
            return "error"
        index = self.find_value(value)
        if index == "Node is not present in the list":
            return "Node is not present in the list"
        elif index == self.length:
            return "last"
        return self.pop(str(index - 1))

    def pop_after(self, value):
        if self.head == None:
            return "error"
        index = self.find_value(value)
        if index == "Node is not present in the list":
            return "Node is not present in the list"
        elif index == self.length - 1:
            return "last"
        return self.pop(str(index + 1))

    def pop_value(self,value):
        if self.head == None:
            return "error"
        index=self.find_value(value)
        if index == "Node is not present in the list":
            return "Node is not present in the list"
        index=int(index)
        if index<0:
            index+=self.length
        if index<0 or index>=self.length:
            return "Index out of range"
        elif index==0:
            return self.pop_front()
        elif index==self.length-1:
            return self.pop_back()
        else:
            node=self.head
            for _ in range(index-1):
                node=node.next
            new_node=node.next
            node.next=new_node.next
            new_node.next.prev=node
            data=new_node.data
            new_node=None
            self.length-=1
            return data
            
    def find_index(self,index):
        if index<0:
            index+=self.length
        if index<0 or index>self.length:
            return "Index out of range"
        current=self.head
        for _ in range(index-1):
            current=current.next
        return current.data

    def find_value(self, value):
        index=0
        flag=False
        current=self.head
        if self.head is None:
            print("List is empty")
            return
        while current is not None:
            if current.data==value:
                flag=True
                break
            current=current.next
            index+=1
        if flag:
            return index
        else:
            return "Node is not present in the list"
    
    def reverse(self):
        current=self.head
        new_node=None
        while current is not None:
            new_node=current.prev
            current.prev=current.next
            current.next=new_node
            current=current.prev
        if new_node is not None:
            self.head=new_node.prev
        
    def print(self):
        current=self.head
        while current:
            print("Current node =",current.data)
            current=current.next

    def clear(self):
        current=self.head
        while current is not None:
            new_node=current
            current=current.next
        self.head=None
        self.length=0

    #Задание 1_5
    def remove_dublicate(self):
        if self.head is None:
            return "error"
        current=self.head
        current.data=str(current.data)
        while current is not None:
            index=current.next
            while index is not None:
                index.data=str(index.data)
                if current.data==index.data:
                    node=index
                    index.prev.next=index.next
                    if index.next is not None:
                        index.next.prev=index.prev
                    node=None
                index=index.next
            current=current.next
                
    #Задание 2_5 часть 1
    def sort_list(self):
        if self.head is None:
            return "No data available"
        current=self.head
        while current is not None:
            new_node=current.next
            current.data=int(current.data)
            while new_node is not None:
                new_node.data=int(new_node.data)
                if current.data>new_node.data:
                    min=new_node.data
                    new_node.data=current.data
                    current.data=min
                new_node=new_node.next
            current=current.next

#Задание 2_5 часть 2
def merge_list(list1,list2):
    if list1.head is None:
        return list2
    if list2.head is None:
        return list1
    result=LinkedList()
    current1=list1.head
    while current1 is not None:
        result.push_back(current1.data)
        current1=current1.next
    list2.sort_list()
    list2.reverse()
    current2=list2.head
    while current2 is not None:
        if current2.data%3==0:
            result.push_back(current2.data)
        current2=current2.next
    return result
    
        

            
l1=LinkedList()
l1.print()
# print("~~~~test_push_front~~~~")
# l1.push_front("222")
# l1.push_front("11")
# l1.push_front("0")
# l1.print()
# print("\n")
# print("~~~~test_push_back~~~~")
# l1.push_back("3")
# l1.push_back("44")
# l1.push_back("555")
# l1.print()
# print("\n")
# # print("~~~~test_push_before~~~~")
# l1.push_before("10","out plus")
# l1.push_before("-10","out minus")
# l1.push_before("0","start")
# l1.push_before("3","six")
# l1.push_before("9","not")
# print(l1.length)
# l1.push_before("555","end")
# l1.print()
# print("\n")
# print("~~~~test_push_after~~~~")
# l1.push_after("10","out plus_2")
# l1.push_after("-10","out minus_2")
# l1.push_after("0","start_2")
# l1.push_after("3","six_2")
# l1.push_after("9","not_2")
# l1.push_after("555","end_2")
# l1.print()
# print("\n")
# print("~~~~test_pop_front~~~~")
# print(l1.pop_front())
# l2=LinkedList()
# print(l2.pop_front())
# l1.print()
# l2.print()
# print("\n")
# print("~~~~test_pop_back~~~~")
# print(l1.pop_back())
# l2=LinkedList()
# print(l2.pop_back())
# l1.print()
# l2.print()
# print("\n")
# print("~~~~test_pop~~~~")
# print(l1.length)
# print(l1.pop("-10"))
# print(l1.pop("7"))
# print(l1.pop("222"))
# print(l1.pop("-222"))
# l2=LinkedList()
# print(l2.pop(0))
# l1.print()
# l2.print()
# print("\n")
# print("~~~~test_pop_before~~~~")
# print(l1.length)
# print(l1.pop_before("-10"))
# print(l1.pop_before("10"))
# print(l1.pop_before("3"))
# print(l1.pop_before("-222"))
# print(l1.pop_before("start"))
# l2=LinkedList()
# print(l2.pop_before("0"))
# l1.print()
# l2.print()
# print("\n")
# print("~~~~test_pop_after~~~~")
# print(l1.length)
# print(l1.pop_after("-10"))
# print(l1.pop_after("10"))
# print(l1.pop_after("3"))
# print(l1.pop_after("-222"))
# print(l1.pop_after("end_2"))
# l2=LinkedList()
# print(l2.pop_after("0"))
# l1.print()
# l2.print()
# print("\n")
# print("~~~~test_pop_value~~~~")
# print(l1.length)
# print(l1.pop_value("-10"))
# print(l1.pop_value("7"))
# print(l1.pop_value("222"))
# print(l1.pop_value("-222"))
# l2=LinkedList()
# print(l2.pop_value("0"))
# l1.print()
# l2.print()
# print("\n")
# print("~~~~test_find_index~~~~")
# print("count =",l1.length)
# print(l1.find_index(6))
# print(l1.find_index(-7))
# print(l1.find_index(-6))
# print(l1.find_index(-2))
# print(l1.find_index(5))
# l1.print()
# print("\n")
# print("~~~~test_reverse~~~~")
# print("normal list:")
# l1.print()
# l2=LinkedList()
# l2.print()
# print("reverse list:")
# l1.reverse()
# l1.print()
# l2.reverse()
# l2.print()
# print("\n")
# print("~~~~test_clear~~~~")
# l1.print()
# l2=LinkedList()
# l2.print()
# print("print after clear:")
# l1.clear()
# l1.print()
# l2.print()
# l2.clear()
# print("end")
# print("\n")
# print("~~~~test_remove_dublicate~~~~")
# l1.push_front(222)
# l1.push_front("11")
# l1.push_front("222")
# l1.push_back(3)
# l1.push_back("22")
# l1.push_back("555")
# l1.push_back(222)
# l1.push_back(555)
# l1.push_back("222")
# l1.push_back(11)
# l1.push_back("2")
# l1.print()
# print("after remove dublicate:")
# l1.remove_dublicate()
# l1.print()
# print("\n")
# print("~~~~test_sort_list~~~~")
# l1.push_front(222)
# l1.push_front(11)
# l1.push_front(0)
# l1.push_back(3)
# l1.push_back(44)
# l1.push_back(555)
# l1.push_back(6)
# l1.print()
# print("list_after_sort:")
# l1.sort_list()
# l1.print()
# print("\n")
# print("~~~~test_merge_sort_list~~~~")
# l1.push_front(0)
# l1.push_front(100)
# l1.push_front(9)
# l1.push_back(-4)
# l2=LinkedList()
# l2.push_back("-5")
# l2.push_back("6")
# l2.push_back("-12")
# l2.push_back(3)
# l2.push_back("33")
# l2.push_back(19)
# l2.push_back(76)
# print("list_1:")
# l1.print()
# print("list_2:")
# l2.print()
# print("after_merge:")
# merge_list(l1,l2).print()
# print("\n")

```

```python
#Взаимодействие с пользователем

from IPython.display import clear_output
# clear_output()

# from time import sleep
# sleep(5.0)

def main():
    print("Введите 'menu', чтобы получить список всех доступных команд с их коротким описанием.")
    print("Введите 'list', если хотите изменять список.")
    print("Введите 'find', чтобы произвести поиск по списку.")
    print("Введите 'reverse', чтобы перевернуть список.")
    print("Введите 'remove dubl', если хотите удалить все повторяющиеся элементы из списка.")
    print("Введите 'merge' для создание нового списка и объединения со старым.")
    print("Введите 'print' для просмотра списка.")
    print("Введите 'stop' для завершения прошраммы.")

print("Пожалуйста введите 'start' чтобы начать.")
x=input()
clear_output()
while x!="start":
    print("Вы ввели неправильную команду. \nПожалуйста введите 'start' чтобы начать.")
    x=input()
    clear_output()
list1=LinkedList()
print("Добро пожаловать!")
while x!="stop":
    main()
    x=input()
    clear_output()
    if x=="menu":
        while x!="end":
            print("Комонда 'menu': вызывается из главной страницы. Она позволяет просмотреть список доступных для пользователя на главной странице команд и дает их короткое описание для понимания за что отвечает каждый раздел.")
            print("Чтобы выйти из этого раздела, необходимо ввести команду 'end'. \n")
            print("Команда 'list': позволяет добавлять элементы в список, удалять элементы, очищать списки, сортировать списк. Добавлять и удалять элементы списка можно в любой последовательности. Невозможно добавить или удалить элемент за пределами списка")
            print("Команда 'find': позволяет найти элемент в списке по заданому индекссу и значению.")
            print("Команда 'reverse': позволяет перевернуть список.")
            print("Команда 'remove dubl': позволяет удалить все повторяющиеся элементы.")
            print("Команда 'merge': позволяет создать новый список и объединить его со старым, отсортировав вновь созданый в обратном порядке и удалив все числа не деляшиеся на 3.")
            print("Команда 'print': ввыводит элементы списка.")
            print("Команда 'stop': позволяет завершить работу программы.")
            x=input()
            clear_output()
    if x=="list":
        while x!="end":
            print("Введите 'add', чтобы добавить элементы в список.")
            print("Введите 'delete', если хотите удалить элементы из списка.")
            print("Введите 'sort', чтобы отсортировать список.")
            print("Введите 'clear', если хотите очистить список.")
            print("Введите 'end', чтобы выйти из этого раздела.")
            x=input()
            clear_output()
            if x=="add":
                while x!="end":
                    print("Введите 'begin', если хотите добавить эллемент в начало списка.")
                    print("Введите 'index', если хотите добавить элемент в любую часть списка.")
                    print("Введите 'before', если хотите добавить элемент перед другим элементом.")
                    print("Введите 'after', если хотите добавить элемент после другого элемента.")
                    print("Введите 'tail', если хотите добавить элемент в конец списка.")
                    print("Введите 'end', чтобы выйти.")
                    x=input()
                    clear_output()
                    if x=="begin":
                        while x!="end":
                            print("Введите количество элементов, которое хотите добавить в начало списка.")
                            count=int(input())
                            for i in range(0,count):
                                print("Введите элемент")
                                element=input()
                                list1.push_front(element)
                            print("Элементы добавлены.")
                            print("Введите 'end', чтобы выйти.")
                            x=input()
                            clear_output()
                    if x=="index":
                        while x!="end":
                            print("Введите количество элементов, которое хотите добавить в список.")
                            count=int(input())
                            for i in range(0,count):
                                print("Введите номер места от 0 до",list1.length,", в которое хотите добавить элемент.")
                                index=int(input())
                                print("Введите элемент, который хотите добавить в список.")
                                element=input()
                                list1.push(index,element)
                            print("Элементы добавлены.")
                            print("Введите 'end', чтобы выйти.")
                            x=input()
                            clear_output()
                    if x=="before":
                        while x!="end":
                            print("Введите количество элементов, которое хотите добавить в список.")
                            count=int(input())
                            for i in range(0,count):
                                print("Введите элемент, перед которым хотите добавить элемент.")
                                value=input()
                                print("Введите элемент, который хотите добавить в список.")
                                element=input()
                                list1.push_before(value,element)
                            print("Элементы добавлены.")
                            print("Введите 'end', чтобы выйти.")
                            x=input()
                            clear_output()
                    if x=="after":
                        while x!="end":
                            print("Введите количество элементов, которое хотите добавить в список.")
                            count=int(input())
                            for i in range(0,count):
                                print("Введите элемент, после которого хотите добавить элемент.")
                                value=input()
                                print("Введите элемент, который хотите добавить в список.")
                                element=input()
                                list1.push_after(value,element)
                            print("Элементы добавлены.")
                            print("Введите 'end', чтобы выйти.")
                            x=input()
                            clear_output()
                    if x=="tail":
                        while x!="end":
                            print("Введите количество элементов, которое хотите добавить в конец списка.")
                            count=int(input())
                            for i in range(0,count):
                                print("Введите элемент")
                                element=input()
                                list1.push_back(element)
                            print("Элементы добавлены.")
                            print("Введите 'end', чтобы выйти.")
                            x=input()
                            clear_output()     
            if x=="delete":
                while x!="end":
                    print("Введите 'begin', если хотите удалить эллемент из начало списка.")
                    print("Введите 'index', если хотите удалить элемент из любую часть списка.")
                    print("Введите 'value', если хотите удалить элемент из любую часть списка.")
                    print("Введите 'before', если хотите удалить элемент перед введеным элементом.")
                    print("Введите 'after', если хотите удалить элемент после введеного элемента.")
                    print("Введите 'tail', если хотите удалить элемент в конеце списка.")
                    print("Введите 'end', чтобы выйти.")
                    x=input()
                    clear_output()
                    if x=="begin":
                        while x!="end":
                            print("Введите количество элементов, которое хотите удалить из начала списка.")
                            count=int(input())
                            for i in range(0,count):
                                list1.pop_front()
                            print("Элементы удалены.")
                            print("Введите 'end', чтобы выйти.")
                            x=input()
                            clear_output()
                    if x=="index":
                        while x!="end":
                            print("Введите количество элементов, которое хотите удалить из списка.")
                            count=int(input())
                            for i in range(0,count):
                                print("Введите номер элемента от 0 до",list1.length-1,", которое хотите удалить.")
                                index=int(input())
                                list1.pop(index)
                            print("Элементы удалены.")
                            print("Введите 'end', чтобы выйти.")
                            x=input()
                            clear_output()
                    if x=="value":
                        while x!="end":
                            print("Введите количество элементов, которое хотите удалить из списка.")
                            count=int(input())
                            for i in range(0,count):
                                print("Введите номер элемента от 0 до",list1.length-1,", которое хотите удалить.")
                                value=input()
                                list1.pop_value(value)
                            print("Элементы удалены.")
                            print("Введите 'end', чтобы выйти.")
                            x=input()
                            clear_output()
                    if x=="before":
                        while x!="end":
                            print("Введите количество элементов, которое хотите удалить из списка.")
                            count=int(input())
                            for i in range(0,count):
                                print("Введите элемент, которое хотите удалить.")
                                value=input()
                                list1.pop_before(value)
                            print("Элементы удалены.")
                            print("Введите 'end', чтобы выйти.")
                            x=input()
                            clear_output()
                    if x=="after":
                        while x!="end":
                            print("Введите количество элементов, которое хотите удалить из списка.")
                            count=int(input())
                            for i in range(0,count):
                                print("Введите номер элемента от 0 до",list1.length-1,", которое хотите удалить.")
                                value=input()
                                list1.pop_after(value)
                            print("Элементы удалены.")
                            print("Введите 'end', чтобы выйти.")
                            x=input()
                            clear_output()
                    if x=="tail":
                        while x!="end":
                            print("Введите количество элементов, которое хотите удалить с конца списка.")
                            count=int(input())
                            for i in range(0,count):
                                list1.pop_back()
                            print("Элементы удалены.")
                            print("Введите 'end', чтобы выйти.")
                            x=input()
                            clear_output() 
            if x=="sort":
                while x!="end":
                    list1.sort_list()
                    print("Ваш список отсортирован.")
                    print("Введите 'end', чтобы выйти.")
                    x=input()
                    clear_output()
            if x=="clear":
                while x!="end":
                    print("Вы точно хотите очистить список? Если да введите 'y', иначе 'n'.")
                    ok=input()
                    if ok=="y":
                        list1.clear()
                        print("Ваш список очищен.")
                    print("Введите 'end', чтобы выйти.")
                    x=input()
                    clear_output()
    if x=="find":
        while x!="end":
            print("Введите 'index', если хотите найти элемент по индексу.")
            print("Введите 'value', если хотите найти элемент по значению.")
            x=input()
            clear_output()
            if x=="index":
                while x!="end":        
                    print("Введите номер элемента от 0 до",list1.length-1,", который хотите найти.")
                    index=int(input())
                    result=list1.find_index(index)
                    print("Под индексом", index, "в списке находится элемент", result)
                    print("Введите 'end', чтобы выйти.")
                    x=input()
                    clear_output()
            if x=="value":
                while x!="end":        
                    print("Введите элемент, который хотите найти.")
                    value=input()
                    index=list1.find_value(value)
                    print("Элемент", value, "в списке находится с индексом", index)
                    print("Введите 'end', чтобы выйти.")
                    x=input()
                    clear_output()
    if x=="reverse":
        while x!="end":
            list1.reverse()
            print("Вы развернули список.")
            print("Введите 'end', чтобы выйти.")
            x=input()
            clear_output()
    if x=="remove dubl":
        while x!="end":
            print("Удаляет в списке все дубликаты")
            print("Так выглядит ваш список перед редактированием.")
            list1.print()
            print("\nВы точно хотите удалить повторяющиеся элементы? Если да введите 'y', иначе 'n'.")
            ok=input()
            if ok=="y":
                list2.remove_dublicate()
                print("Повторяющиеся элементы удалены.")
                print("Теперь ваш список выглядит так:")
                list1.print()
            print("\nВведите 'end', чтобы выйти.")
            x=input()
            clear_output() 
    if x=="merge":
        while x!="end":
            print("Создайте список. Для этого введите сколько элементов должно быть в новом списке.")
            list2=LinkedList()
            print("Введите количество элементов.")
            count=int(input())
            for i in range(0,count):
                print("Введите элемент")
                element=input()
                list2.push_back(element)
            clear_output() 
            print("Так выглядит изначальный список.")
            list1.print()
            print("\nТак выглядит ваш список после заполнения.")
            list2.print()
            print("\nВы точно хотите объединить старый и новый список? Если да введите 'y', иначе 'n'. Итоговый список будет отсортирован!")
            ok=input()
            if ok=="y":
                list1=merge_list(list1,list2)
                print("Списки объединены.")
                print("Теперь ваш список выглядит так:")
                list1.print()
            print("\nВведите 'end', чтобы выйти.")
            x=input()
            clear_output() 
    if x=="print":
        while x!="end":
            print("Сейчас ваш список выглядит так.")
            list1.print()
            print("Введите 'end', чтобы выйти.")
            x=input()
            clear_output()
print("Программа завершина.\nВсего доброго.")








```

```python

```

```python

```

```python

```

```python

```
