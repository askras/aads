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
<h1> ОТЧЕТ </h1>
<h3> Лабораторная работа №8 <br> <br>
    «Алгоритмы на графах» </h3>
<br>
<h4> Цель работы: </h4>
Изучение основных алгоритмов на графах.
<br>
<br>
<h4> Постановка задачи: </h4>

1. Реализовать программу, выполняющую описанный набор операций на графах:<br>
Требования:
 - граф должен быть реализован в виде класса;
 - каждая операция должна быть реализована как метод класса.
   
2. Реализовать приложение, для работы с графом, которое реализует следующий набор действий:
   - инициализация графа;
   - организация диалогового цикла с пользователем;
3. Реализовать индивидуальные задание.
<br>
<br>
<h4> Code Listing: </h4>

```python

```
<br>
<h4> Выводы </h4>
В ходе лабораторной работы была реализована программа, выполняющая стандартный набор операций на графах и организован диалоговый цикл с пользователем.
<br>
<br>
<h4> Ответы на контрольные вопросы </h4>

1. *Что такое граф? Что такое ребро и дуга графа?* <br>
Граф - это математическая абстракция, которая состоит из множества вершин и множества ребер, соединяющих эти вершины. Ребро - это связь между двумя вершинами, а дуга - направленное ребро, указывающее на направление от одной вершины к другой.
2. *Что такое ориентированный граф и неориентированный граф?* <br>
Ориентированный граф - это граф, в котором каждое ребро имеет определенное направление, в то время как неориентированный граф не имеет направления на своих ребрах.
3. *Какие вершины называют смежными? Какие ребра называют смежными? Что означает слово инцидентные?* <br>
Вершины называют смежными, если они соединены ребром. Ребра называют смежными, если они имеют общую вершину. Слово "инцидентные" означает, что вершина инцидентна ребру.
4. *Что такое вес вершины, вес ребра?* <br>
Вес вершины или ребра - это дополнительная информация, связанная с вершиной или ребром, которая может использоваться в различных алгоритмах обработки графов, например, в алгоритмах поиска кратчайшего пути.
5. *Какие способы представления графов существуют?* <br>
Графы могут быть представлены с помощью матриц смежности, матриц инцидентности, списка смежности или списка ребер.
6. *В чем разница между алгоритмами поиска в ширину и поиска в глубину?* <br>
Алгоритм поиска в ширину начинает с одной вершины и поочередно обходит все смежные с ней вершины, прежде чем переходить к следующей вершине. В то время как алгоритм поиска в глубину идет как можно глубже, прежде чем вернуться и перейти к следующей ветви.
7. *Описать алгоритм нахождения кратчайшего пути.* <br>
Алгоритм нахождения кратчайшего пути, например, алгоритм Дейкстры или алгоритм Флойда-Уоршалла, используется для нахождения минимального пути от одной вершины к другой во взвешенном графе.
8. *Описать алгоритмы нахождения эйлерова и гамильтонова цикла.* <br>
Эйлеров цикл проходит через каждое ребро ровно один раз, в то время как гамильтонов цикл проходит через каждую вершину ровно один раз. Алгоритмы для их нахождения различаются и могут быть реализованы с использованием различных подходов, таких как эйлеров обход или алгоритмы поиска гамильтонова цикла.
<!-- #endregion -->

```python
class LoserError(Exception):
    def __init__(self, *args):
        if args:
            self.message = args[0]
        else:
            self.message = None

    def __str__(self):
        if self.message:
            return f'LoserError: {self.message}'
        else:
            return 'YOU LOSER'

class Graph:
    def init(self):
        self.vertices = {}

    def __str__(self):
        for vertex in self.vertices:
            print(f"{vertex}: {', '.join(map(str, self.vertices[vertex]))}")

    def add_vertex(self, vertex):
        if vertex not in self.vertices:
            self.vertices[vertex] = []
        else:
            raise LoserError()

    def add_edge(self, first, second):
        if first in self.vertices and second in self.vertices:
            self.vertices[first].append(second)
            self.vertices[second].append(first)
        else:
            raise LoserError()

    def remove_vertex(self, vertex):
        if vertex in self.vertices:
            del self.vertices[vertex]
            for i in self.vertices:
                for j in self.verteces[i]:
                    if vertex == j:
                        deleted = self.verteces[i].pop(vertex)
        else:
            raise LoserError()

    def remove_edge(self, first, second):
        if first in self.vertices and second in self.vertices:
            for i in self.vertices[first]:
                if i == second:
                    deleted = self.verteces[first].pop(i)
            for i in self.vertices[second]:
                if i == first:
                    deleted = self.verteces[second].pop(i)
        else:
            raise LoserError()

graph = Graph()
# Обход (поиск) в глубину
def dfs_depth(graph, first, visited=[]):
    if first not in visited:
        visited.appsecond(first)
        for next in graph[first]:
            dfs_depth(graph,next,visited)
    return visited


graph = {
    'A':['B','S'],
    'B':['A'],
    'C':['D','E','F','S'],
    'D':['C'],
    'E':['C','H'],
    'F':['C','G'],
    'G':['F','S'],
    'H':['E','G'],
    'S':['A','C','G']
}

# Взаимодействие с пользователем
x = input("Добро пожаловать!\nЕсли вы хотите вывести набор команд: введите Menu\nЕсли вы хотите посмотреть граф: введите Show\nЕсли вы хотите проверить пустое ли граф: введите Is Empty\nЕсли вы хотите добавить элементы в граф: введите Add\nЕсли вы хотите удалить элементы из графа: введите Remove\nЕсли вы хотите очистить граф: введите Clear\nЕсли вы хотите закончить: введите Stop\n")
mytree = Graph()
while True:
    x = x.lower()
    match x:
        case "menu":
            print("Если вы хотите вывести набор команд: введите Menu\nЕсли вы хотите посмотреть граф: введите Show\nЕсли вы хотите проверить пустое ли граф: введите Is Empty\nЕсли вы хотите добавить элементы в граф: введите Add\nЕсли вы хотите обойти граф: введите Traversal\nЕсли вы хотите узнать распоожение элемента в графе: введите Find Item\nЕсли вы хотите удалить элементы из графа: введите Remove\nЕсли вы хотите узнать глубину графа: введите Depth\nЕсли вы хотите очистить граф: введите Clear\nЕсли вы хотите найти произведение элементов всех четных уровней: введите Product Even Levels\nЕсли вы хотите закончить: введите Stop\n")
        case "show":
            print(mytree)
        case "is empty":
            if mytree.is_empty(mytree.root):
                print("Граф пустое")
            else:
                print("Граф не пустое")
        case "add":
            message = input("Если вы хотите линейно заполнить граф: введите Fill, если же добавить один элемент: введите Add\n")
            if not message.isalpha():
                print("YOU LOSER")
                print("Надо было ввести команду :З")
            else:
                if message == "fill":
                    length = input("Введите количество элементов которое хотите добавить: ")
                    if not length.isdigit():
                        print("YOU LOSER")
                        print("Надо было ввести число :З")
                    else:
                        print("Если вдруг вы устанете заполнять граф и захотите прервать процесс: введите ~I'm LoSeR~")
                        count_elements = 0
                        for i in range(0, int(length)):

                            item = input("Введите элемент: ")
                            if item == "~I'm LoSeR~":
                                print("Элементы успешно добавились, процесс прерван")
                                break
                            else:
                                try:
                                    mytree.add(item)
                                except ValueError:
                                    print("Такой элемент уже есть в графе")
                                except TypeError:
                                    print("В граф можно добавлять только числа")
                                count_elements += 1
                        if count_elements == length:
                            print("Граф успешно заполнено")
                elif message == "add":
                    item = input("Введите элемент: ")
                    flag = True
                    try:
                        mytree.add(item)
                    except ValueError:
                        flag = False
                        print("Такой элемент уже есть в графе")
                    except TypeError:
                        flag = False
                        print("В граф можно добавлять только числа")
                    if flag:
                        print("Вы добавили элемент", item)
                else:
                    print("YOU LOSER")
                    print("Вы ввели неправильную команду :З")
        case "remove":
            message = input("Если вы хотите удалить несколько элементов: введите Remove, если один: введите Pop")
            if not message.isalpha():
                print("YOU LOSER")
                print("Надо было ввести команду :З")
            else:
                message = message.lower()
                if message == "remove":
                    length = input("Введите количество элементов для удаления: ")
                    if not length.isdigit():
                        print("YOU LOSER")
                        print("В следующий раз стоит вводить корректное количество элементов для удаления :З")
                    else:
                        print("Если вдруг вы устанете удалять элементы и захотите прервать процесс: введите ~I'm LoSeR~")
                        for i in range(0, int(length)):
                            item = input("Введите элемент, который хотите удалить: ")
                            if item == "~I'm LoSeR~":
                                print("Элементы успешно удалены, процесс прерван")
                                break
                            else:
                                try:
                                    mytree.remove(item)
                                    print("Вы удалили элемент", item)
                                except TypeError:
                                    print("YOU LOSER")
                                    print("А что вы собрались удалять в пустом графе (｡· v ·｡)?")
                                except ValueError:
                                    print("В графе присутствуют только целочисленные элементы")
                elif message == "pop":
                    item = input("Введите элемент, который хотите удалить: ")
                    try:
                        mytree.remove(item)
                        print("Вы удалили элемент", item)
                    except TypeError:
                        print("YOU LOSER")
                        print("А что вы собрались удалять в пустом графе (｡· v ·｡)?")
                    except ValueError:
                        print("В графе присутствуют только целочисленные элементы")
                else:
                        print("YOU LOSER")
                        print("Вы ввели неправильную команду :З")
        case "depth":
            print("Глубина графа:", mytree.depth(mytree.root, 0))
        case "clear":
            try:
                mytree.clear()
                print("Вы очистили граф, его элементы больше не доступны :(")
            except TypeError:
                print("YOU LOSER")
                print("Не стоит пытаться очистить пустое граф :З")
        case "stop":
            break
        case _:
            print("Научись вводить команды правильно :З")
    x = input("Введите еще команду: ")

```
