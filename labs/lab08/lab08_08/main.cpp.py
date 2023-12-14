class dieError(Exception):
    def __init__(self, *args):
        super().__init__(*args)

    def __str__(self):
        return "dieError: " + " ".join(map(str, self.args))


class DirectedGraph:
    def __init__(self):
        self.graph = {}

    def add_edge(self, first, second, weight=1):
        if first in self.graph and second in self.graph:
            self.graph[first].append((second, weight))
        else:
            raise dieError("One or more vertices not found in the graph.")

    def __str__(self):
        return str(self.graph)

    def is_empty(self):
        return not bool(self.graph)

    def add_vertex(self, vertex):
        if vertex not in self.graph:
            self.graph[vertex] = []

    def remove_vertex(self, vertex):
        if vertex in self.graph:
            del self.graph[vertex]
            for v in self.graph:
                self.graph[v] = [(u, w) for u, w in self.graph[v] if u != vertex]

    def remove_edge(self, first, second):
        if first in self.graph and second in self.graph:
            self.graph[first] = [(u, w) for u, w in self.graph[first] if u != second]

    def clear(self):
        self.graph.clear()

    def copy(self):
        new_graph = DirectedGraph()
        new_graph.graph = {vertex: list(neighbors) for vertex, neighbors in self.graph.items()}
        return new_graph

    def depth_traversal(self, vertex, visited_vertices):
        visited_vertices.add(vertex)
        for neighbor, _ in self.graph[vertex]:
            if neighbor not in visited_vertices:
                self.depth_traversal(neighbor, visited_vertices)

    def width_traversal(self, vertex, visited_vertices, queue, result):
        visited_vertices.add(vertex)
        queue.append(vertex)
        while queue:
            current_vertex = queue.pop(0)
            result.append(current_vertex)
            for neighbor, _ in self.graph[current_vertex]:
                if neighbor not in visited_vertices:
                    visited_vertices.add(neighbor)
                    queue.append(neighbor)

    def eulerian_cycle(self):
        def eulerian_cycle_util(current, cycle):
            while self.graph[current]:
                neighbor, _ = self.graph[current].pop()
                eulerian_cycle_util(neighbor, cycle)
            cycle.append(current)

        visited_vertices = set()
        self.depth_traversal(next(iter(self.graph)), visited_vertices)
        if len(visited_vertices) != len(self.graph):
            return None

        for vertex in self.graph:
            in_degree = sum(1 for _, edges in self.graph.items() for neighbor, _ in edges if neighbor == vertex)
            out_degree = len(self.graph[vertex])
            if in_degree != out_degree:
                return None

        start_vertex = next(iter(self.graph)) if self.graph else None
        if start_vertex is None:
            return None

        cycle = []
        eulerian_cycle_util(start_vertex, cycle)

        return cycle[::-1]
    def hamiltonian_cycle(self):
        def hamiltonian_util(current, visited, path):
            visited[current] = True
            path.append(current)

            if len(path) == len(self.graph):
                if path[0] in [v for v, _ in self.graph[path[-1]]]:
                    path.append(path[0])
                    return path

            for vertex, _ in self.graph[current]:
                if not visited[vertex]:
                    result = hamiltonian_util(vertex, visited.copy(), path.copy())
                    if result:
                        return result

            return None

        start_vertex = next(iter(self.graph)) if self.graph else None
        if start_vertex is None:
            return None

        visited = {vertex: False for vertex in self.graph}
        return hamiltonian_util(start_vertex, visited, [])

    def dijkstra_shortest_path(self, start):
        if start not in self.graph:
            return None

        distances = {vertex: float('inf') for vertex in self.graph}
        distances[start] = 0
        visited = set()

        while len(visited) < len(self.graph):
            current = min(
                (vertex for vertex in self.graph if vertex not in visited),
                key=lambda x: distances[x]
            )
            visited.add(current)

            for neighbor, weight in self.graph[current]:
                new_distance = distances[current] + weight
                if new_distance < distances[neighbor]:
                    distances[neighbor] = new_distance

        return distances


class UndirectedGraph(DirectedGraph):
    def add_edge(self, first, second, weight=1):
        super().add_edge(first, second, weight)
        self.graph[second].append((first, weight))

    def remove_edge(self, first, second):
        super().remove_edge(first, second)
        self.graph[second] = [(u, w) for u, w in self.graph[second] if u != first]

    def eulerian_cycle(self):
        def eulerian_cycle_util(current, visited, cycle):
            visited[current] = True

            for neighbor, weight in self.graph[current]:
                if not visited[neighbor]:
                    eulerian_cycle_util(neighbor, visited, cycle)

            cycle.append(current)
            return cycle

        start_vertex = next(iter(self.graph)) if self.graph else None
        if start_vertex is None:
            return None

        visited = {vertex: False for vertex in self.graph}
        cycle = eulerian_cycle_util(start_vertex, visited, [])

        for vertex in self.graph:
            for neighbor, _ in self.graph[vertex]:
                if not visited[neighbor]:
                    return None  # Граф не связный

        return list(dict.fromkeys(cycle[::-1]))

    def depth_traversal(self, vertex, visited_vertices):
        visited_vertices.add(vertex)
        for neighbor, _ in self.graph[vertex]:
            if neighbor not in visited_vertices:
                self.depth_traversal(neighbor, visited_vertices)


class GraphApplication:
    def __init__(self, graph):
        self.graph = graph

    @classmethod
    def create_graph(cls, graph_type):
        if graph_type == "directed":
            return cls(DirectedGraph())
        elif graph_type == "undirected":
            return cls(UndirectedGraph())
        else:
            raise dieError("Unsupported graph type. Use 'directed' or 'undirected'.")

    def print_menu(self):
        print("\n===== Меню приложения =====")
        print("1. Добавить вершину")
        print("2. Добавить ребро")
        print("3. Удалить вершину")
        print("4. Удалить ребро")
        print("5. Вывести граф")
        print("6. Обход в глубину")
        print("7. Обход в ширину")
        print("8. Эйлеров цикл (для неориентированных графов)")
        print("9. Гамильтонов цикл")
        print("10. Кратчайший путь (алгоритм Дейкстры)")
        print("0. Выход")

    def run(self):
        while True:
            self.print_menu()
            choice = input("Выберите действие (введите номер): ")

            if choice == "0":
                print("Выход из приложения. До свидания!")
                break

            try:
                if choice == "1":
                    vertex = input("Введите название вершины: ")
                    self.graph.add_vertex(vertex)
                    print(f"Вершина {vertex} добавлена.")

                elif choice == "2":
                    start = input("Введите начальную вершину: ")
                    end = input("Введите конечную вершину: ")
                    weight = int(input("Введите вес ребра: "))
                    self.graph.add_edge(start, end, weight)
                    print(f"Ребро ({start}, {end}) добавлено с весом {weight}.")

                elif choice == "3":
                    vertex = input("Введите название вершины: ")
                    self.graph.remove_vertex(vertex)
                    print(f"Вершина {vertex} удалена.")

                elif choice == "4":
                    start = input("Введите начальную вершину: ")
                    end = input("Введите конечную вершину: ")
                    self.graph.remove_edge(start, end)
                    print(f"Ребро ({start}, {end}) удалено.")

                elif choice == "5":
                    print("Текущий граф:")
                    print(self.graph)

                elif choice == "6":
                    start_vertex = input("Введите стартовую вершину для обхода в глубину: ")
                    visited_vertices = set()
                    result = []
                    self.graph.depth_traversal(start_vertex, visited_vertices)
                    print(f"Обход в глубину: {list(visited_vertices)}")

                elif choice == "7":
                    start_vertex = input("Введите стартовую вершину для обхода в ширину: ")
                    visited_vertices = set()
                    queue = []
                    result = []
                    self.graph.width_traversal(start_vertex, visited_vertices, queue, result)
                    print(f"Обход в ширину: {result}")

                elif choice == "8":
                    if isinstance(self.graph, UndirectedGraph):
                        cycle = self.graph.eulerian_cycle()
                        print(f"Эйлеров цикл: {cycle}")
                    else:
                        print("Эйлеров цикл применим только к неориентированным графам.")

                elif choice == "9":
                    cycle = self.graph.hamiltonian_cycle()
                    print(f"Гамильтонов цикл: {cycle}")

                elif choice == "10":
                    start_vertex = input("Введите начальную вершину для алгоритма Дейкстры: ")
                    distances = self.graph.dijkstra_shortest_path(start_vertex)
                    print("Кратчайшие пути:")
                    for vertex, distance in distances.items():
                        print(f"До вершины {vertex}: {distance}")

                else:
                    print("Неверный ввод. Пожалуйста, введите номер операции из меню.")

            except Exception as e:
                print(f"Ошибка: {e}")

graph_type = input("Выберите тип графа ('directed' или 'undirected'): ")
app = GraphApplication.create_graph(graph_type)
app.run()