class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class CircularSinglyList:
    def __init__(self):
        self.head = None
        self.length = 0


    def push_front(self, data):
        new_node = Node(data)
        if self.length == 0:
            new_node.next = new_node
        else:
            current = self.head
            while current.next != self.head:
                current = current.next
            current.next = new_node
            new_node.next = self.head
        self.head = new_node
        self.length += 1


    def push_before(self, value, data):
        new_node = Node(data)
        if self.length == 0:
            print("List is empty")
            return
        current = self.head
        while True:
            if current.next is None:
                break
            if current.next.data == value:
                new_node.next = current.next
                current.next = new_node
                self.length += 1
                return
            current = current.next
            if current == self.head:
                break
        print("Node not found in the list")


    def push_after(self, value, data):
        new_node = Node(data)
        if self.length == 0:
            print("List is empty")
            return
        current = self.head
        while True:
            if current.next is None:
                break
            if current.data == value:
                new_node.next = current.next
                current.next = new_node
                self.length += 1
                if current == self.head:
                    self.head = new_node
                return
            current = current.next
            if current == self.head:
                break
        print("Node not found in the list")


    def push_back(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.head.next = self.head
        else:
            current = self.head
            while current.next != self.head:
                current = current.next
            current.next = new_node
            new_node.next = self.head
        self.length += 1


    def pop_front(self):
        if self.length == 0:
            print("List is empty.")
            return
        if self.head.next == self.head:
            self.head = None
        else:
            current = self.head
            while current.next != self.head:
                current = current.next
            current.next = self.head.next
            self.head = self.head.next
        self.length -= 1


    def pop_before(self, value):
        if self.length == 0:
            print("List is empty.")
            return
        current = self.head
        while current.next.data != value:
            current = current.next
        previous = current.next
        previous.next = previous.next.next
        if current == self.head:
            self.head = previous.next
        self.length -= 1


    def pop_after(self, value):
        if self.length == 0:
            print("List is empty.")
            return
        current = self.head
        while current.data != value:
            current = current.next
            if current == self.head:
                return self
        if current.next == self.head:
            return self
        current.next = current.next.next
        if current.next == self.head:
            self.head = current.next.next
        self.length -= 1


    def delete_node(self, value):
        if self.length == 0:
            print("List is empty.")
            return
        if self.head.data == value:
            self.head = self.head.next
            self.length -= 1
            return self
        current = self.head
        prev = None
        while current is not None and current.data != value:
            prev = current
            current = current.next
        if current is None:
            return self
        prev.next = current.next
        self.length -= 1


    def pop_back(self):
        if self.length == 0:
            print("List is empty.")
            return
        if self.head.next is None:
            self.head = None
            self.length -= 1
            return
        current = self.head
        prev = None
        while current.next != self.head:
            prev = current
            current = current.next
        prev.next = self.head
        self.length -= 1


    def at(self, value):
        if self.length == 0:
            print("List is empty.")
            return
        current = self.head
        while True:
            if current.data == value:
                return current
            current = current.next
            if current == self.head:
                break
        return


    def clear(self):
        self.head = None
        self.length = 0


    def reverse(self):
        if self.head is None:
            return
        current = self.head
        previous = None
        while True:
            next_ = current.next
            current.next = previous
            previous = current
            current = next_
            if current == self.head:
                break
        self.head = previous


    def split_list(L):
        L1 = CircularSinglyList()
        L2 = CircularSinglyList()
        current = L.head
        while True:
            if current.data > 0:
                L1.push_back(current.data)
            else:
                L2.push_back(current.data)

            current = current.next

            if current == L.head:
                break
        return L1, L2


    def average(self):
        if self.length == 0:
            return None
        current = self.head
        total = current.data
        while current.next != self.head:
            current = current.next
            total += current.data
        return total / self.length


    def display(self):
        if self.length == 0:
            print("List is empty.")
            return
        temp = self.head
        while True:
            if temp is not None:
                print(temp.data, end=" -> ")
                temp = temp.next
                if temp == self.head:
                    print("...")
                    break
            else:
                break


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
        print("10. Из L сделать полож. L1 и отриц. L2")
        print("11. Добавить элемент перед указанным значением")
        print("12. Добавить элемент после указанного значения")
        print("13. Удалить элемент перед указанным значением")
        print("14. Удалить элемент после указанного значения")
        print("15. Среднее арифметическое")
        print("16. Очистить текущий список")
        print("17. Удалить по значению")
        print("0. Выход")

        choice = input("Введите ваш выбор: ")

        if choice == '1':
            new_list = CircularSinglyList()
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
            current_list.pop_front()
        elif choice == '6':
            current_list.pop_back()
        elif choice == '7':
            current_list.reverse()
        elif choice == '8':
            value = int(input("Введите значение для поиска: "))
            current_list.at(value)
        elif choice == '9':
            current_list.display()
        elif choice == '10':
            L1, L2 = current_list.split_list()
            L1.display()
            L2.display()
        elif choice == '11':
            data = int(input("Введите данные: "))
            value = int(input("Введите значение, перед которым нужно вставить элемент: "))
            current_list.push_before(data, value)
        elif choice == '12':
            data = int(input("Введите данные: "))
            value = int(input("Введите значение, после которого нужно вставить элемент: "))
            current_list.push_after(data, value)
        elif choice == '13':
            value = int(input("Введите значение, перед которым нужно удалить элемент: "))
            current_list.pop_before(value)
        elif choice == '14':
            value = int(input("Введите значение, после которого нужно удалить элемент: "))
            current_list.pop_after(value)
        elif choice == '15':
            print(current_list.average())
        elif choice == '16':
            current_list.clear()
            print("Список очищен.")
        elif choice == '17':
            value = int(input("Введите значение, которое нужно удалить элемент: "))
            current_list.delete_node(value)
        elif choice == '0':
            break
        else:
            print("Неверный выбор. Пожалуйста, выберите допустимую операцию.")


if __name__ == "__main__":
    main()
