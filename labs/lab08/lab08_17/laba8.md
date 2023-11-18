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

1. Реализовать программу, выполняющую описанный набор операций на графах, приэтом
    - граф должен быть реализован в виде класса;
    - каждая операция должна быть реализована как метод класса
2. Реализовать приложение, для работы с графом, которое реализует следующий набор действий
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

class DirectedGraph:
    def __init__(self):
        self.vertices = {}

    def __str__(self):
        if self.is_empty():
            text = "The graph is empty: None"
            return text
        else:
            for vertex in self.vertices:
                print(f"{vertex}: {', '.join(map(str, self.vertices[vertex]))}")
            return ""

    def is_empty(self):
        if self.vertices == {}:
            return True
        else:
            return False

    def add_vertex(self, vertex):
        if vertex not in self.vertices:
            self.vertices[vertex] = []
        else:
            raise LoserError()

    def add_edge(self, first, second):
        if first in self.vertices and second in self.vertices:
            self.vertices[first].append(second)
        else:
            raise LoserError()

    def remove_vertex(self, vertex):
        if self.is_empty():
            raise TypeError("empty")
        if vertex in self.vertices:
            del self.vertices[vertex]
            for i in self.vertices:
                for j in self.vertices[i]:
                    if j == vertex:
                        self.vertices[i].remove(vertex)
        else:
            raise LoserError()

    def remove_edge(self, first, second):
        if self.is_empty():
            raise TypeError("empty")
        if first in self.vertices and second in self.vertices:
            for i in self.vertices[first]:
                if i == second:
                    self.vertices[first].remove(i)
        else:
            raise LoserError()

    def clear(self):
        self.vertices = {}

    def depth_traversal(self, vertex, visited_vertices):
        if self.is_empty():
            raise LoserError()
        if vertex not in visited_vertices:
            visited_vertices.append(vertex)
            for i in self.vertices[vertex]:
                self.depth_traversal(i, visited_vertices)
        return visited_vertices

    # from collections import deque
    def width_traversal(self, vertex, visited_vertices):
        if self.is_empty():
            raise LoserError()
        if vertex not in visited_vertices:
            visited_vertices.append(vertex)
            for i in self.vertices[vertex]:
                self.depth_traversal(i, visited_vertices)
        return visited_vertices
        # visited = set()
        # queue = deque([start])
        # visited.add(start)
        # while queue:
        #     vertex = queue.popleft()
        #     for neighbour in graph[vertex]:
        #         if neighbour not in visited:
        #             visited.add(neighbour)
        #             queue.append(neighbour)
        # return visited

class UndirectedGraph:
    def __init__(self):
        self.vertices = {}

    def __str__(self):
        if self.is_empty():
            text = "The graph is empty: None"
            return text
        else:
            for vertex in self.vertices:
                print(f"{vertex}: {', '.join(map(str, self.vertices[vertex]))}")
            return ""

    def is_empty(self):
        if self.vertices == {}:
            return True
        else:
            return False

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
        if self.is_empty():
            raise TypeError("empty")
        if vertex in self.vertices:
            del self.vertices[vertex]
            for i in self.vertices:
                for j in self.vertices[i]:
                    if j == vertex:
                        self.vertices[i].remove(vertex)
        else:
            raise LoserError()

    def remove_edge(self, first, second):
        if self.is_empty():
            raise TypeError("empty")
        if first in self.vertices and second in self.vertices:
            for i in self.vertices[first]:
                if i == second:
                    self.vertices[first].remove(i)
            for i in self.vertices[second]:
                if i == first:
                    self.vertices[second].remove(i)
        else:
            raise LoserError()

    def clear(self):
        self.vertices = {}

    def depth_traversal(self, vertex, visited_vertices):
        if self.is_empty():
            raise LoserError()
        if vertex not in visited_vertices:
            visited_vertices.append(vertex)
            for i in self.vertices[vertex]:
                self.depth_traversal(i, visited_vertices)
        return visited_vertices


# Взаимодействие с пользователем
graph = input("Добро пожаловать!\nЕсли вы хотите работать с ориентированным графом: введите Directed, если же с неориентированным: введите Undirected\n")
flag = True
while True:
    if flag == False:
        break
    if graph.lower() == "directed":
        mygraph = DirectedGraph()
        print("Вы создали ориентированный граф")
        x = input("Добро пожаловать!\nЕсли вы хотите вывести набор команд: введите Menu\nЕсли вы хотите посмотреть граф: введите Show\nЕсли вы хотите проверить пустой ли граф: введите Is Empty\nЕсли вы хотите добавить вершину в граф: введите Add Vertex\nЕсли вы хотите добавить ребро в граф: введите Add Edge\nЕсли вы хотите удалить вершину из графа: введите Remove Vertex\nЕсли вы хотите удалить ребро из графа: введите Remove Edge\nЕсли вы хотите очистить граф: введите Clear\nЕсли вы хотите закончить: введите Stop\n")
        while True:
            x = x.lower()
            match x:
                case "menu":
                    print("Если вы хотите вывести набор команд: введите Menu\nЕсли вы хотите посмотреть граф: введите Show\nЕсли вы хотите проверить пустое ли граф: введите Is Empty\nЕсли вы хотите добавить элементы в граф: введите Add\nЕсли вы хотите обойти граф: введите Traversal\nЕсли вы хотите узнать распоожение элемента в графе: введите Find Item\nЕсли вы хотите удалить элементы из графа: введите Remove\nЕсли вы хотите узнать глубину графа: введите Depth\nЕсли вы хотите очистить граф: введите Clear\nЕсли вы хотите найти произведение элементов всех четных уровней: введите Product Even Levels\nЕсли вы хотите закончить: введите Stop\n")
                case "show":
                    print(mygraph)
                case "is empty":
                    if mygraph.is_empty():
                        print("Граф пустой")
                    else:
                        print("Граф не пустой")
                case "add vertex":
                    message = input("Если вы хотите добавить несколько вершин: введите Fill, если же одну: введите Add\n")
                    if not message.isalpha():
                        print("YOU LOSER")
                        print("Надо было ввести команду :З")
                    else:
                        if message == "fill":
                            length = input("Введите количество вершин которое хотите добавить: ")
                            if not length.isdigit():
                                print("YOU LOSER")
                                print("Надо было ввести число :З")
                            else:
                                print("Если вдруг вы устанете заполнять граф и захотите прервать процесс: введите ~I'm LoSeR~")
                                count_elements = 0
                                f1 = True
                                for i in range(0, int(length)):
                                    if not f1:
                                        break
                                    item = input("Введите вершину: ")
                                    if item == "~I'm LoSeR~":
                                        while True:
                                            exit = input("Если вы хотите закончить добавление вершин: введите Break, если добавить вершину ~I'm LoSeR~: введите Add\n")
                                            if not exit.isalpha():
                                                print("YOU LOSER")
                                                print("Надо было ввести команду :З")
                                                print("Попробуйте еще раз")
                                            else:
                                                exit = exit.lower() 
                                                if exit == "break":
                                                    print("Вершины успешно добавлены, процесс прерван")
                                                    f1 = False
                                                    break
                                                elif exit == "add":
                                                    try:
                                                        mygraph.add_vertex(item)
                                                    except LoserError as message:
                                                        print(message)
                                                        print("Такая вершина уже есть в графе")
                                                    count_elements += 1
                                                    break
                                                else:
                                                    print("YOU LOSER")
                                                    print("Надо было ввести команду :З")
                                                    print("Попробуйте еще раз")
                                    else:
                                        try:
                                            mygraph.add_vertex(item)
                                        except LoserError as message:
                                            print(message)
                                            print("Такой элемент уже есть в графе")
                                        count_elements += 1
                                if count_elements == length:
                                    print("Вершины успешно добалены")
                        elif message == "add":
                            item = input("Введите вершину: ")
                            f2 = True
                            try:
                                mygraph.add_vertex(item)
                            except LoserError as message:
                                f2 = False
                                print(message)
                                print("Такая вершина уже есть в графе")
                            if f2:
                                print("Вершина успешно добавлена")
                        else:
                            print("YOU LOSER")
                            print("Вы ввели неправильную команду :З")
                case "add edge":
                    message = input("Если вы хотите добавить несколько ребер: введите Fill, если же одно: введите Add\n")
                    if not message.isalpha():
                        print("YOU LOSER")
                        print("Надо было ввести команду :З")
                    else:
                        if message == "fill":
                            length = input("Введите количество ребер, которое хотите добавить: ")
                            if not length.isdigit():
                                print("YOU LOSER")
                                print("Надо было ввести число :З")
                            else:
                                print("Если вдруг вы устанете заполнять граф и захотите прервать процесс: введите ~I'm LoSeR~ в любой из элементов")
                                count_elements = 0
                                f1 = True
                                for i in range(0, int(length)):
                                    if not f1:
                                        break
                                    first = input("Введите вершину, из которой должно выходить ребро: ")
                                    second = input("Введите вершину, в которую должно входить ребро: ")
                                    if first == "~I'm LoSeR~" or second == "~I'm LoSeR~":
                                        while True:
                                            exit = input("Если вы хотите закончить добавление ребер: введите Break, если добавить ребро с вершиной ~I'm LoSeR~: введите Add\n")
                                            if not exit.isalpha():
                                                print("YOU LOSER")
                                                print("Надо было ввести команду :З")
                                                print("Попробуйте еще раз")
                                            else:
                                                exit = exit.lower() 
                                                if exit == "break":
                                                    print("Ребра успешно добавлены, процесс прерван")
                                                    f1 = False
                                                    break
                                                elif exit == "add":
                                                    try:
                                                        mygraph.add_edge(first, second)
                                                    except LoserError as message:
                                                        print(message)
                                                        print("Вы уверены что эти вершины есть в графе (｡· v ·｡)?")
                                                    count_elements += 1
                                                    break
                                                else:
                                                    print("YOU LOSER")
                                                    print("Надо было ввести команду :З")
                                                    print("Попробуйте еще раз")
                                    else:
                                        try:
                                            mygraph.add_edge(first, second)
                                        except LoserError as message:
                                            print(message)
                                            print("Вы уверены что эти вершины есть в графе (｡· v ·｡)?")
                                        count_elements += 1
                                if count_elements == length:
                                    print("Ребра успешно добалены")
                        elif message == "add":
                            first = input("Введите вершину, из которой должно выходить ребро: ")
                            second = input("Введите вершину, в которую должно входить ребро: ")
                            f2 = True
                            try:
                                mygraph.add_edge(first, second)
                            except LoserError as message:
                                f2 = False
                                print(message)
                                print("Вы уверены что эти вершины есть в графе (｡· v ·｡)?")
                            if f2:
                                print("Ребро успешно добавлено")
                        else:
                            print("YOU LOSER")
                            print("Вы ввели неправильную команду :З")
                case "remove vertex":
                    item = input("Введите вершину, которую хотите удалить: ")
                    try:
                        mygraph.remove_vertex(item)
                        print("Вы удалили вершину", item)
                    except TypeError:
                        print("YOU LOSER")
                        print("А что вы собрались удалять в пустом графе (｡· v ·｡)?")
                    except LoserError as message:
                        print(message)
                        print("Вы уверены что этa вершинa есть в графе (｡· v ·｡)?")
                case "remove edge":
                    first = input("Введите вершину, из которой выходит ребро: ")
                    second = input("Введите вершину, в которую входит ребро: ")
                    try:
                        mygraph.remove_edge(first, second)
                        print("Вы успешно удалили ребро")
                    except TypeError:
                        print("YOU LOSER")
                        print("А что вы собрались удалять в пустом графе (｡· v ·｡)?")
                    except LoserError as message:
                        print(message)
                        print("Вы уверены что это ребро есть в графе (｡· v ·｡)?")
                case "depth traversal":
                    try:
                        print(mygraph.depth_traversal(list(mygraph.vertices.keys())[0], []))
                    except IndexError:
                        print("YOU LOSER")
                        print("Граф путой")
                case "clear":
                    try:
                        mygraph.clear()
                        print("Вы очистили граф, его элементы больше не доступны :(")
                    except TypeError:
                        print("YOU LOSER")
                        print("Не стоит пытаться очистить пустой граф :З")
                case "stop":
                    flag = False
                    break
                case _:
                    print("Научись вводить команды правильно :З")
            x = input("Введите еще команду: ")
    elif graph.lower() == "undirected":
        mygraph = UndirectedGraph()
        print("Вы создали неориентированный граф")
        x = input("Добро пожаловать!\nЕсли вы хотите вывести набор команд: введите Menu\nЕсли вы хотите посмотреть граф: введите Show\nЕсли вы хотите проверить пустой ли граф: введите Is Empty\nЕсли вы хотите добавить вершину в граф: введите Add Vertex\nЕсли вы хотите добавить ребро в граф: введите Add Edge\nЕсли вы хотите удалить вершину из графа: введите Remove Vertex\nЕсли вы хотите удалить ребро из графа: введите Remove Edge\nЕсли вы хотите очистить граф: введите Clear\nЕсли вы хотите закончить: введите Stop\n")
        while True:
            x = x.lower()
            match x:
                case "menu":
                    print("Если вы хотите вывести набор команд: введите Menu\nЕсли вы хотите посмотреть граф: введите Show\nЕсли вы хотите проверить пустое ли граф: введите Is Empty\nЕсли вы хотите добавить элементы в граф: введите Add\nЕсли вы хотите обойти граф: введите Traversal\nЕсли вы хотите узнать распоожение элемента в графе: введите Find Item\nЕсли вы хотите удалить элементы из графа: введите Remove\nЕсли вы хотите узнать глубину графа: введите Depth\nЕсли вы хотите очистить граф: введите Clear\nЕсли вы хотите найти произведение элементов всех четных уровней: введите Product Even Levels\nЕсли вы хотите закончить: введите Stop\n")
                case "show":
                    print(mygraph)
                case "is empty":
                    if mygraph.is_empty():
                        print("Граф пустой")
                    else:
                        print("Граф не пустой")
                case "add vertex":
                    message = input("Если вы хотите добавить несколько вершин: введите Fill, если же одну: введите Add\n")
                    if not message.isalpha():
                        print("YOU LOSER")
                        print("Надо было ввести команду :З")
                    else:
                        if message == "fill":
                            length = input("Введите количество вершин которое хотите добавить: ")
                            if not length.isdigit():
                                print("YOU LOSER")
                                print("Надо было ввести число :З")
                            else:
                                print("Если вдруг вы устанете заполнять граф и захотите прервать процесс: введите ~I'm LoSeR~")
                                count_elements = 0
                                f1 = True
                                for i in range(0, int(length)):
                                    if not f1:
                                        break
                                    item = input("Введите вершину: ")
                                    if item == "~I'm LoSeR~":
                                        while True:
                                            exit = input("Если вы хотите закончить добавление вершин: введите Break, если добавить вершину ~I'm LoSeR~: введите Add\n")
                                            if not exit.isalpha():
                                                print("YOU LOSER")
                                                print("Надо было ввести команду :З")
                                                print("Попробуйте еще раз")
                                            else:
                                                exit = exit.lower() 
                                                if exit == "break":
                                                    print("Вершины успешно добавлены, процесс прерван")
                                                    f1 = False
                                                    break
                                                elif exit == "add":
                                                    try:
                                                        mygraph.add_vertex(item)
                                                    except LoserError as message:
                                                        print(message)
                                                        print("Такая вершина уже есть в графе")
                                                    count_elements += 1
                                                    break
                                                else:
                                                    print("YOU LOSER")
                                                    print("Надо было ввести команду :З")
                                                    print("Попробуйте еще раз")
                                    else:
                                        try:
                                            mygraph.add_vertex(item)
                                        except LoserError as message:
                                            print(message)
                                            print("Такой элемент уже есть в графе")
                                        count_elements += 1
                                if count_elements == length:
                                    print("Вершины успешно добалены")
                        elif message == "add":
                            item = input("Введите вершину: ")
                            f2 = True
                            try:
                                mygraph.add_vertex(item)
                            except LoserError as message:
                                f2 = False
                                print(message)
                                print("Такая вершина уже есть в графе")
                            if f2:
                                print("Вершина успешно добавлена")
                        else:
                            print("YOU LOSER")
                            print("Вы ввели неправильную команду :З")
                case "add edge":
                    message = input("Если вы хотите добавить несколько ребер: введите Fill, если же одно: введите Add\n")
                    if not message.isalpha():
                        print("YOU LOSER")
                        print("Надо было ввести команду :З")
                    else:
                        if message == "fill":
                            length = input("Введите количество ребер, которое хотите добавить: ")
                            if not length.isdigit():
                                print("YOU LOSER")
                                print("Надо было ввести число :З")
                            else:
                                print("Если вдруг вы устанете заполнять граф и захотите прервать процесс: введите ~I'm LoSeR~ в любой из элементов")
                                count_elements = 0
                                f1 = True
                                for i in range(0, int(length)):
                                    if not f1:
                                        break
                                    first = input("Введите первую вершину: ")
                                    second = input("Введите вторую вершину: ")
                                    if first == "~I'm LoSeR~" or second == "~I'm LoSeR~":
                                        while True:
                                            exit = input("Если вы хотите закончить добавление ребер: введите Break, если добавить ребро с вершиной ~I'm LoSeR~: введите Add\n")
                                            if not exit.isalpha():
                                                print("YOU LOSER")
                                                print("Надо было ввести команду :З")
                                                print("Попробуйте еще раз")
                                            else:
                                                exit = exit.lower() 
                                                if exit == "break":
                                                    print("Ребра успешно добавлены, процесс прерван")
                                                    f1 = False
                                                    break
                                                elif exit == "add":
                                                    try:
                                                        mygraph.add_edge(first, second)
                                                    except LoserError as message:
                                                        print(message)
                                                        print("Вы уверены что эти вершины есть в графе (｡· v ·｡)?")
                                                    count_elements += 1
                                                    break
                                                else:
                                                    print("YOU LOSER")
                                                    print("Надо было ввести команду :З")
                                                    print("Попробуйте еще раз")
                                    else:
                                        try:
                                            mygraph.add_edge(first, second)
                                        except LoserError as message:
                                            print(message)
                                            print("Вы уверены что эти вершины есть в графе (｡· v ·｡)?")
                                        count_elements += 1
                                if count_elements == length:
                                    print("Ребра успешно добалены")
                        elif message == "add":
                            first = input("Введите первую вершину: ")
                            second = input("Введите вторую вершину: ")
                            f2 = True
                            try:
                                mygraph.add_edge(first, second)
                            except LoserError as message:
                                f2 = False
                                print(message)
                                print("Вы уверены что эти вершины есть в графе (｡· v ·｡)?")
                            if f2:
                                print("Ребро успешно добавлено")
                        else:
                            print("YOU LOSER")
                            print("Вы ввели неправильную команду :З")
                case "remove vertex":
                    item = input("Введите вершину, которую хотите удалить: ")
                    try:
                        mygraph.remove_vertex(item)
                        print("Вы удалили вершину", item)
                    except TypeError:
                        print("YOU LOSER")
                        print("А что вы собрались удалять в пустом графе (｡· v ·｡)?")
                    except LoserError as message:
                        print(message)

                        print("Вы уверены что этa вершинa есть в графе (｡· v ·｡)?")
                case "remove edge":
                    first = input("Введите первую вершину: ")
                    second = input("Введите вторую вершину: ")
                    try:
                        mygraph.remove_edge(first, second)
                        print("Вы успешно удалили ребро")
                    except TypeError:
                        print("YOU LOSER")
                        print("А что вы собрались удалять в пустом графе (｡· v ·｡)?")
                    except LoserError as message:
                        print(message)
                        print("Вы уверены что это ребро есть в графе (｡· v ·｡)?")
                case "clear":
                    try:
                        mygraph.clear()
                        print("Вы очистили граф, его элементы больше не доступны :(")
                    except TypeError:
                        print("YOU LOSER")
                        print("Не стоит пытаться очистить пустой граф :З")
                case "stop":
                    flag = False
                    break
                case _:
                    print("Научись вводить команды правильно :З")
            x = input("Введите еще команду: ")
    else:
        graph = input("Попробуйте ввести что-то из предложенных вариантов :З\n")
```

```python
class DirectedGraph:
    def __init__(self):
        self.vertices = {}

    def __str__(self):
        if self.is_empty():
            text = "The graph is empty: None"
            return text
        else:
            for vertex in self.vertices:
                print(f"{vertex}: {', '.join(map(str, self.vertices[vertex]))}")
            return ""

    def is_empty(self):
        if self.vertices == {}:
            return True
        else:
            return False

    def add_vertex(self, vertex):
        if vertex not in self.vertices:
            self.vertices[vertex] = []
        else:
            raise LoserError()

    def add_edge(self, first, second):
        if first in self.vertices and second in self.vertices:
            self.vertices[first].append(second)
        else:
            raise LoserError()

    def remove_vertex(self, vertex):
        if self.is_empty():
            raise TypeError("empty")
        if vertex in self.vertices:
            del self.vertices[vertex]
            for i in self.vertices:
                for j in self.vertices[i]:
                    if j == vertex:
                        self.vertices[i].remove(vertex)
        else:
            raise LoserError()

    def remove_edge(self, first, second):
        if self.is_empty():
            raise TypeError("empty")
        if first in self.vertices and second in self.vertices:
            for i in self.vertices[first]:
                if i == second:
                    self.vertices[first].remove(i)
        else:
            raise LoserError()

    def clear(self):
        self.vertices = {}

    def depth_traversal(self, vertex, visited_vertices):
        if self.is_empty():
            raise LoserError()
        if vertex not in visited_vertices:
            visited_vertices.append(vertex)
            for i in self.vertices[vertex]:
                self.depth_traversal(i, visited_vertices)
        return visited_vertices

    # from collections import deque
    # def bfs_breadth(graph, start):
    #     visited = set()
    #     queue = deque([start])
    #     visited.add(start)
    #     while queue:
    #         vertex = queue.popleft()
    #         for neighbour in graph[vertex]:
    #             if neighbour not in visited:
    #                 visited.add(neighbour)
    #                 queue.append(neighbour)
    #     return visited

    def width_traversal(self, vertex, visited_vertices, queue, result):
        if vertex in visited_vertices:
            return result
        visited_vertices.add(vertex)
        result.append(vertex)
        for i in self.vertices[vertex]:
            if not i in visited_vertices:
                queue.append(i)
        while queue:
            width_traversal(queue.pop(0))
        return result
        
    # def width_traversal(self, vertex, visited_vertices):
    #     if self.is_empty():
    #         raise LoserError()
    #     if vertex not in visited_vertices:
    #         visited_vertices.append(vertex)
    #         for i in self.vertices[vertex]:
    #             self.depth_traversal(i, visited_vertices)
    #     return visited_vertices

a = DirectedGraph()
a.add_vertex(1)
a.add_vertex(2)
a.add_vertex(3)
a.add_vertex(4)
a.add_vertex(5)
print(a)
a.add_edge(1, 2)
a.add_edge(2, 3)
a.add_edge(3, 4)
a.add_edge(4, 5)
a.add_edge(5, 1)
a.add_edge(1, 3)
a.add_edge(4, 2)
a.add_edge(1, 5)
# a.add_edge(4, 5)
# a.add_edge(5, 1)
print(a)
print(a.depth_traversal(list(a.vertices.keys())[0], []))
print(a.width_traversal(list(a.vertices.keys())[0], set(), [], []))
```

```python

```
