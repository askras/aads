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

## Лабораторная работа №4

### Линейный однонаправленный список

### Цель работы:

Изучение структуры данных «Циклические однонаправленные списки», а также основных операций над ними.

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

- Написать функцию, которая оставляет в списке L только последние вхождения одинаковых элементов.
- Пусть имеется список L. Удалить из него каждый третий элемент.

### Листинг программного кода с описанием

class Node:
    def __init__(self,data)

class LinkedList:
    def __init__(self)
        
    def push_front(self, data) # Добавляет элемент в начало списка
    
    def push_back(self,data) # Добавляет элемент в коней списка

    def push(self,index,data) # Добавляет элемент в указаное место в списке
    
    def pop_front(self) # Удаляет первй элемент списка
    
    def pop_back(self) # Удаляет последний элемент списка

    def pop(self,index) # Удаляет указаный элемент списка

    def find_index(self,index) # Находит элемент по индексу

    def find_value(self, value) # ищет индекс элемента по значению
    
    def reverse(self) # Переворачивает список

    def print(self) # Выводит список

    def clear(self) # Очищает список

    def remove_dublicate(self) # удаляет все повторяющиеся элементы

    def remove_third(self) # удаляет каждый третий элемент

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

                    if x=="tail" # добавляет элемент в конце
  
                        while x!="end" # возвращает в главное меню
    
            if x=="delete" # содержит команды удаления
  
                while x!="end" # возвращает в главное меню
  
                    if x=="begin" # удаляет в начале
  
                        while x!="end" # возвращает в главное меню
   
                    if x=="index" # удаляет по индексу
  
                        while x!="end" # возвращает в главное меню

                    if x=="tail" # удаляет в конце
  
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

    if x=="remove third" # оудаляет каждый третий элемент
  
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

5. Дать определение циклического списка.

Циклический (кольцевой) список – это структура данных, представляющая собой последовательность элементов, последний элемент которой содержит указатель на первый элемент списка, а первый (в случае двунаправленного списка) – на последний.
Основная особенность такой организации состоит в том, что в этом списке нет элементов, содержащих пустые указатели, и, следовательно, нельзя выделить крайние элементы.

6. Классификация циклических списков.

- Односвязный циклический список: каждый узел ОЦС содержит 1 поле указателя на следующий узел; поле указателя последнего узла содержит адрес первого узла (корня списка)
- Двусвязный циклический список: каждый узел ДЦС содержит два поля указателей: на следующий и на предыдущий узел; поле указателя на следующий узел последнего узла содержит адрес первого узла (корня списка); поле указателя на предыдущий узел первого узла (корня списка) содержит адрес последнего узла

7. Какие основные операции выполняются над циклическим списком?

- Добавление и удаление элементов
- Нахождение элементов
- Переворачивание списка




<!-- #endregion -->

```python

class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class LinkedList:
    def __init__(self):
        self.head=None
        self.tail=None
        # self.head.next=self.tail
        # self.tail.next=self.head
        self.length=0
        
    def push_front(self, data):
        new_node=Node(data)
        if self.head is None:
            self.head=new_node
            self.tail=new_node
            new_node.next=self.head
        else:
            new_node.next=self.head
            self.head=new_node
            self.tail.next=self.head
        self.length+=1
        return data
    
    def push_back(self,data):
        new_node=Node(data)
        if self.head is None:
            self.head=new_node
            self.tail=new_node
            new_node.next=self.head
        else:
            self.tail.next=new_node
            self.tail=new_node
            self.tail.next=self.head
        self.length+=1
        return data

    def push(self,index,data):
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
            current.next=new_node
            self.length+=1
            return data
    
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
        old_head=None
        self.tail.next=self.head
        self.length-=1
        return data
    
    def pop_back(self):
        if self.head is None:
            return "Insufficient data"
        old_tail=self.tail
        data=old_tail.data
        if self.length==1:
            self.head=None
            self.tail=None
        elif self.head!=self.tail:
            current=self.head
            while current.next!=self.tail:
                current=current.next
            self.tail=current
            self.tail.next=self.head
        self.length-=1
        return data

    def pop(self,index):
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
            data=new_node.data
            # del new_node
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
        while current!=self.tail:
            if str(current.data)==str(value):
                flag=True
                break
            current=current.next
            index+=1
        if flag:
            return index
        else:
            return "Node is not present in the list"
    
    def reverse(self):
        if self.head is None:
            return "Not list"
        current=self.head
        prev_node=None
        while True:
            new_node=current.next
            current.next=prev_node
            prev_node=current
            current=new_node
            if current==self.head:
                break
        self.head=prev_node
        head=self.head.next
        tail=self.head
        while head!=None:
            tail=tail.next
            head=head.next
        self.tail=tail
        tail.next=self.head

    def print(self):
        current=self.head
        if self.head is None:
            print("List is empty")
            return
        while True:
            print("Current node =",current.data)
            current=current.next
            if current==self.head:
                break
    
    def clear(self):
        if self.head is None:
            print("List clean")
            return
        current=self.head.next
        while current!=self.head:
            new_node=current
            current=current.next
            del new_node
        self.head=None
        self.tail=None
        self.length=0
        
    #Задание 1_5
    def remove_dublicate(self):
        if self.head is None:
            return "error"
        self.reverse()
        current=self.head
        current.data=str(current.data)
        # while current.next!=self.head:
        while True:
            node=current
            index=current.next
            while index!=self.head:
                index.data=str(index.data)
                if current.data==index.data:
                    node.next=index.next
                else:
                    node=index
                index=index.next
            current=current.next
            if current.next==self.head:
                break
        self.reverse()
                
    #Задание 2_5 часть 1
    def remove_third(self):
        if self.head is None:
            return "error"
        current=self.head
        count=1
        index=0
        size=self.length
        while True:
            if count%3==0:
                self.pop(index)
                index-=1
            index+=1
            count+=1
            if current.next==self.head:
                break
            current=current.next
        return size
    
        

            
l1=LinkedList()
# l1.print()
# print("~~~~test_push_front~~~~")
# l1.push_front(222)
# l1.push_front(11)
# l1.push_front(0)
# l1.print()
# print("\n")
# print("~~~~test_push_back~~~~")
# l1.push_back(3)
# l1.push_back(44)
# l1.push_back(555)
# l1.print()
# print("\n")
# print("~~~~test_push~~~~")
# l1.push(10,"out plus")
# l1.push(-10,"out minus")
# l1.push(0,"start")
# l1.push(-2,"six")
# l1.push(9,"not")
# print(l1.length)
# l1.push(8,"end")
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
# print(l1.pop(-10))
# print(l1.pop(7))
# print(l1.pop(2))
# print(l1.pop(-2))
# l2=LinkedList()
# print(l2.pop(0))
# l1.print()
# l2.print()
# print("\n")
# print("~~~~test_find_index~~~~")
# print("count =",l1.length)
# print(l1.find_index(6))
# print(l1.find_index(-6))
# print(l1.find_index(-5))
# print(l1.find_index(-2))
# print(l1.find_index(5))
# l1.print()
# print("\n")
# print("~~~~test_find_value~~~~")
# print(l1.find_value("555"))
# print(l1.find_value(11))
# print(l1.find_value("insert"))
# print(l1.find_value(22))
# l1.print()
# print("\n")
# print("~~~~test_reverse~~~~")
# print(l1.head.data, l1.tail.data)
# print("normal list:")
# l1.print()
# l2=LinkedList()
# l2.print()
# print("reverse list:")
# l1.reverse()
# l1.print()
# l2.reverse()
# l2.print()
# print(l1.head.data, l1.tail.data)
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
# print("~~~~test_remove_third~~~~")
# l1.push_front(222)
# l1.push_front(11)
# l1.push_front(0)
# l1.push_back(3)
# l1.push_back(44)
# l1.push_back(555)
# l1.push_back(6)
# l1.print()
# print(l1.length)
# print("after remove third:")
# l1.remove_third()
# print(l1.length)
# l1.print()
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
    print("Введите 'remove third' для удаления каждого третьего элемента.")
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
            print("Команда 'remove third': позволяет удалить каждый третий элемент в списке.")
            print("Команда 'print': ввыводит элементы списка.")
            print("Команда 'stop': позволяет завершить работу программы.")
            x=input()
            clear_output()
    if x=="list":
        while x!="end":
            print("Введите 'add', чтобы добавить элементы в список.")
            print("Введите 'delete', если хотите удалить элементы из списка.")
            print("Введите 'clear', если хотите очистить список.")
            print("Введите 'end', чтобы выйти из этого раздела.")
            x=input()
            clear_output()
            if x=="add":
                while x!="end":
                    print("Введите 'begin', если хотите добавить эллемент в начало списка.")
                    print("Введите 'index', если хотите добавить элемент в любую часть списка.")
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
                list1.remove_dublicate()
                print("Повторяющиеся элементы удалены.")
                print("Теперь ваш список выглядит так:")
                list1.print()
            print("\nВведите 'end', чтобы выйти.")
            x=input()
            clear_output() 
    if x=="remove third":
        while x!="end":
            print("\nВы точно хотите удалить каждый третий элемент? Если да введите 'y', иначе 'n'. Итоговый список будет отсортирован!")
            ok=input()
            if ok=="y":
                list1.remove_third()
                print("Список обнавлен.")
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
