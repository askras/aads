class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class List:
    def __init__(self):
        self.head = None
        self.length = 0

    def push_front(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.length += 1

    def pop_front(self):
        if self.head is None:
            return None
        old_head = self.head
        data = old_head.data
        if self.length == 1:
            self.head = None
        else:
            self.head = old_head.next
        self.length -= 1
        return data

    def __iter__(self):
        self.current = self.head
        return self

    def __next__(self):
        if self.current is None:
            raise StopIteration
        data = self.current.data
        self.current = self.current.next
        return data

    def push_back(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node
        self.length += 1

    def pop_back(self):
        if self.head is None:
            return None

        if self.length == 1:
            data = self.head.data
            self.head = None
            self.length -= 1
            return data

        current = self.head
        while current.next.next:
            current = current.next

        data = current.next.data
        current.next = None
        self.length -= 1
        return data

    def at(self, index):
        if index < 0:
            index += self.length
        if index < 0 or index >= self.length:
            raise IndexError("Index out of range")

        current = self.head
        for _ in range(index):
            current = current.next
        return current.data

    def push(self, data, index):
        if index == 0:
            self.push_front(data)
        elif index == self.length:
            self.push_back(data)
        elif index > 0 and index < self.length:
            new_node = Node(data)
            current = self.head
            for _ in range(index - 1):
                current = current.next
            new_node.next = current.next
            current.next = new_node
            self.length += 1
        else:
            raise IndexError("Index out of range")

    def pop(self, index):
        if index == 0:
            return self.pop_front()
        elif index == self.length - 1:
            return self.pop_back()
        elif index > 0 and index < self.length - 1:
            current = self.head
            for _ in range(index - 1):
                current = current.next
            node_to_remove = current.next
            current.next = node_to_remove.next
            data = node_to_remove.data
            del node_to_remove
            self.length -= 1
            return data
        else:
            raise IndexError("Index out of range")

    def clear(self):
        while self.head:
            node_to_remove = self.head
            self.head = self.head.next
            del node_to_remove
        self.length = 0

    def reverse(self):
        prev = None
        current = self.head
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        self.head = prev

    def find(self, value):
        current = self.head
        index = 0
        while current:
            if current.data == value:
                return index
            current = current.next
            index += 1
        return -1

    def display(self):
        current = self.head
        while current:
            print(current.data, end=' -> ')
            current = current.next
        print("None")


def intersect_lists(list1, list2):
    intersection = List()
    current1 = list1.head

    while current1:
        current2 = list2.head
        while current2:
            if current1.data == current2.data:
                intersection.push_back(current1.data)
            current2 = current2.next
        current1 = current1.next

    return intersection


def multiply_lists(list1, list2):
    result = List()

    current1 = list1.head
    current2 = list2.head

    while current1 and current2:
        result.push_back(current1.data * current2.data)
        current1 = current1.next
        current2 = current2.next

    return result


def main():
    lists = []
    current_list = None

    while True:
        print("\nВыберите операцию:")
        print("1. Создать новый список")
        print("2. Выбрать существующий список")
        print("3. Добавить элемент в начало")
        print("4. Добавить элемент в конец")
        print("5. Удалить элемент с начала")
        print("6. Удалить элемент с конца")
        print("7. Реверс списка")
        print("8. Найти элемент")
        print("9. Вывести список")
        print("10. Пересечение двух списков")
        print("11. Умножение двух списков")
        print("12. Очистить текущий список")
        print("0. Выход")

        choice = input("Введите ваш выбор: ")

        if choice == '1':
            new_list = List()
            lists.append(new_list)
            current_list = new_list
            print("Создан новый список.")
        elif choice == '2':
            if len(lists) > 0:
                print("Выберите список (0 -", len(lists) - 1, "):")
                for i, l in enumerate(lists):
                    print(i, "-", "Длина:", l.length)
                list_choice = int(input())
                if 0 <= list_choice < len(lists):
                    current_list = lists[list_choice]
                    print("Выбран список с длиной", current_list.length)
                else:
                    print("Неверный выбор списка.")
            else:
                print("Нет созданных списков.")
        elif choice == '3':
            data = int(input("Введите данные: "))
            current_list.push_front(data)
        elif choice == '4':
            data = int(input("Введите данные: "))
            current_list.push_back(data)
        elif choice == '5':
            data = current_list.pop_front()
            print(f"Удаленный элемент: {data}")
        elif choice == '6':
            data = current_list.pop_back()
            print(f"Удаленный элемент: {data}")
        elif choice == '7':
            current_list.reverse()
            print("Список перевернут.")
        elif choice == '8':
            value = int(input("Введите значение для поиска: "))
            index = current_list.find(value)
            if index != -1:
                print(f"Значение {value} найдено по индексу {index}.")
            else:
                print(f"Значение {value} не найдено.")
        elif choice == '9':
            current_list.display()
        elif choice == '10':
            if len(lists) < 2:
                print("Для выполнения операции необходимо создать или выбрать минимум два списка.")
            else:

                print("Выберите два списка для пересечения:")
                for i, l in enumerate(lists):
                    print(i, "-", "Длина:", l.length)
                list_choice_1 = int(input("Выберите первый список: "))
                list_choice_2 = int(input("Выберите второй список: "))
                if 0 <= list_choice_1 < len(lists) and 0 <= list_choice_2 < len(lists):
                    list1 = lists[list_choice_1]
                    list2 = lists[list_choice_2]
                    intersection = intersect_lists(list1, list2)
                    print("Пересечение двух списков:")
                    intersection.display()
                else:
                    print("Неверный выбор списка.")
        elif choice == '11':
            if len(lists) < 2:
                print("Для выполнения операции необходимо создать или выбрать минимум два списка.")
            else:

                print("Выберите два списка для умножения:")
                for i, l in enumerate(lists):
                    print(i, "-", "Длина:", l.length)
                list_choice_1 = int(input("Выберите первый список: "))
                list_choice_2 = int(input("Выберите второй список: "))
                if 0 <= list_choice_1 < len(lists) and 0 <= list_choice_2 < len(lists):
                    list1 = lists[list_choice_1]
                    list2 = lists[list_choice_2]
                    result_list = multiply_lists(list1, list2)
                    print("Результат умножения двух списков:")
                    result_list.display()
                else:
                    print("Неверный выбор списка.")
        elif choice == '12':
            current_list.clear()
            print("Список очищен.")
        elif choice == '0':
            break
        else:
            print("Неверный выбор. Пожалуйста, выберите допустимую операцию.")

if __name__ == "__main__":
    main()