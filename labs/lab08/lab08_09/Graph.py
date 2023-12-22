import heapq

class Graph:
    def __init__(self, num_vertices):
        self.num_vertices = num_vertices
        self.adjacency_matrix = [[0] * num_vertices for _ in range(num_vertices)]
        self.incidence_matrix = [[0] * num_vertices for _ in range(num_vertices)]
        self.weight_matrix = [[float('inf')] * num_vertices for _ in range(num_vertices)]
        self.adjacency_list = [[] for _ in range(num_vertices)]

    def add_edge(self, start, end, weight=None):
        self.adjacency_matrix[start][end] = 1
        self.incidence_matrix[start][end] = 1
        self.incidence_matrix[end][start] = -1
        self.adjacency_list[start].append((end, weight))  # Используем пары (вершина, вес)
        self.weight_matrix[start][end] = weight if weight is not None else float('inf')

    def print_adjacency_matrix(self):
        print("Матрица смежности:")
        for row in self.adjacency_matrix:
            print(row)

    def print_incidence_matrix(self):
        print("Матрица инцидентности:")
        for row in self.incidence_matrix:
            print(row)

    def print_weight_matrix(self):
        print("Матрица весов:")
        for row in self.weight_matrix:
            print(row)

    def print_adjacency_list(self):
        print("Списки смежных вершин:")
        for i, adj_list in enumerate(self.adjacency_list):
            print(f"{i}: {adj_list}")

    def depth_first_search(self, start_vertex):
        visited = [False] * self.num_vertices
        stack = [start_vertex]
        result = []

        while stack:
            current_vertex = stack.pop()
            if not visited[current_vertex]:
                visited[current_vertex] = True
                result.append(current_vertex)

                for neighbor, _ in self.adjacency_list[current_vertex]:
                    if not visited[neighbor]:
                        stack.append(neighbor)

        return result

    def breadth_first_search(self, start_vertex):
        visited = [False] * self.num_vertices
        queue = [start_vertex]
        result = []

        while queue:
            current_vertex = queue.pop(0)
            if not visited[current_vertex]:
                visited[current_vertex] = True
                result.append(current_vertex)

                for neighbor, _ in self.adjacency_list[current_vertex]:
                    if not visited[neighbor]:
                        queue.append(neighbor)

        return result

    def eulerian_cycle(self):
        if not self.is_connected() or not self.is_all_vertices_even_degree():
            return None

        start_vertex = next(iter(self.adjacency_list))

        stack = [start_vertex]

        cycle = []

        while stack:
            current_vertex = stack[-1]

            if self.adjacency_list[current_vertex]:
                next_vertex, _ = self.adjacency_list[current_vertex].pop()
                stack.append(next_vertex)
                self.remove_edge(current_vertex, next_vertex)
            else:
                cycle.append(stack.pop())

        return cycle[::-1]

    def hamiltonian_cycle(self):
        start_vertex = next(iter(self.adjacency_list))

        stack = [start_vertex]

        visited = {start_vertex}

        cycle = []

        while stack:
            current_vertex = stack[-1]

            next_vertex = self.get_unvisited_neighbor(current_vertex, visited)

            if next_vertex is not None:
                visited.add(next_vertex)
                stack.append(next_vertex)
                cycle.append((current_vertex, next_vertex))
            else:
                stack.pop()

        return cycle if len(cycle) == self.num_vertices else None  # Проверяем, что это гамильтонов цикл

    def get_unvisited_neighbor(self, vertex, visited):
        for neighbor in self.adjacency_list[vertex]:
            if neighbor not in visited:
                return neighbor
        return None

    def is_connected(self):
        visited = set()
        self.dfs_connected(next(iter(self.adjacency_list)), visited)
        return len(visited) == self.num_vertices

    def dfs_connected(self, vertex, visited):
        visited.add(vertex)
        for neighbor, _ in self.adjacency_list[vertex]:
            if neighbor not in visited:
                self.dfs_connected(neighbor, visited)

    def is_all_vertices_even_degree(self):
        for vertex in range(self.num_vertices):
            if len(self.adjacency_list[vertex]) % 2 != 0:
                return False
        return True

    def dijkstra(self, start_vertex, end_vertex):
        if start_vertex not in range(self.num_vertices) or end_vertex not in range(self.num_vertices):
            return float('inf'), []

        distances = [float('inf')] * self.num_vertices
        distances[start_vertex] = 0
        previous_vertices = [None] * self.num_vertices
        visited = set()
        priority_queue = [(0, start_vertex)]

        while priority_queue:
            current_distance, current_vertex = heapq.heappop(priority_queue)

            if current_vertex in visited:
                continue

            visited.add(current_vertex)

            for neighbor, weight in self.adjacency_list[current_vertex]:
                new_distance = distances[current_vertex] + weight
                if new_distance < distances[neighbor]:
                    distances[neighbor] = new_distance
                    previous_vertices[neighbor] = current_vertex
                    heapq.heappush(priority_queue, (new_distance, neighbor))

        if distances[end_vertex] == float('inf'):
            return float('inf'), []

        path = []
        current_vertex = end_vertex
        total_weight = distances[end_vertex]  # Теперь суммарный вес равен дистанции до конечной вершины
        while current_vertex is not None:
            path.append(current_vertex)
            current_vertex = previous_vertices[current_vertex]

        path = path[::-1]
        return total_weight, path

    def remove_edge(self, current_vertex, next_vertex):
        pass


graph = Graph(5)
graph.add_edge(0, 1, 1)
graph.add_edge(0, 2, 9)
graph.add_edge(1, 3, 3)
graph.add_edge(2, 4, 4)

graph.print_adjacency_matrix()
graph.print_incidence_matrix()
graph.print_weight_matrix()
graph.print_adjacency_list()

dfs_result = graph.depth_first_search(0)
print("DFS:", dfs_result)

bfs_result = graph.breadth_first_search(0)
print("BFS:", bfs_result)

total_weight, path = graph.dijkstra(0, 4)
print(f"Shortest distance from vertex 0 to 4: {total_weight}")
print(f"Shortest path from vertex 0 to 4: {path}")



graph = Graph(5)

# Добавляем рёбра с весами
graph.add_edge(0, 1, 2)
graph.add_edge(1, 2, 3)
graph.add_edge(2, 3, 1)
graph.add_edge(3, 4, 4)
graph.add_edge(4, 0, 5)

graph.print_adjacency_matrix()
graph.print_weight_matrix()

def interactive_graph():
    while True:
        print("\nВыберите действие:")
        print("1. Создать граф")
        print("2. Вывести матрицы графа")
        print("3. Выполнить DFS (Depth-First Search)")
        print("4. Выполнить BFS (Breadth-First Search)")
        print("5. Выполнить Dijkstra's Algorithm")
        print("6. Проверить связность графа")
        print("7. Выйти")

        choice = input("Введите номер действия: ")

        if choice == "1":
            num_vertices = int(input("Введите количество вершин графа: "))
            graph = Graph(num_vertices)

            while True:
                print("\nВыберите действие:")
                print("1. Добавить ребро")
                print("2. Вернуться в предыдущее меню")

                sub_choice = input("Введите номер действия: ")

                if sub_choice == "1":
                    start = int(input("Введите начальную вершину: "))
                    end = int(input("Введите конечную вершину: "))
                    weight = int(input("Введите вес ребра (если неориентированный граф, введите 0): "))
                    graph.add_edge(start, end, weight)
                elif sub_choice == "2":
                    break
                else:
                    print("Некорректный выбор. Попробуйте еще раз.")

        elif choice == "2":
            graph.print_adjacency_matrix()
            graph.print_incidence_matrix()
            graph.print_weight_matrix()
            graph.print_adjacency_list()

        elif choice == "3":
            start_vertex = int(input("Введите начальную вершину для DFS: "))
            dfs_result = graph.depth_first_search(start_vertex)
            print(f"DFS: {dfs_result}")

        elif choice == "4":
            start_vertex = int(input("Введите начальную вершину для BFS: "))
            bfs_result = graph.breadth_first_search(start_vertex)
            print(f"BFS: {bfs_result}")

        elif choice == "5":
            start_vertex = int(input("Введите начальную вершину для Dijkstra's Algorithm: "))
            end_vertex = int(input("Введите конечную вершину для Dijkstra's Algorithm: "))
            total_weight, path = graph.dijkstra(start_vertex, end_vertex)
            print(f"Кратчайшее расстояние: {total_weight}")
            print(f"Кратчайший путь: {path}")

        elif choice == "6":
            connected = graph.is_connected()
            print(f"Граф {'связен' if connected else 'не связен'}.")

        elif choice == "7":
            print("Программа завершена.")
            break

        else:
            print("Некорректный выбор. Попробуйте еще раз.")

if __name__ == "__main__":
    interactive_graph()

