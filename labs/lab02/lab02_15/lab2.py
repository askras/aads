class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def push_front(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def push_back(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def insert(self, index, data):
        if index < 0:
            raise IndexError("Недопустимый индекс")
        if index == 0:
            self.push_front(data)
            return
        new_node = Node(data)
        current = self.head
        for i in range(index - 1):
            if current is None:
                raise IndexError("Недопустимый индекс")
            current = current.next
        if current is None:
            raise IndexError("Недопустимый индекс")
        new_node.next = current.next
        current.next = new_node

    def pop_front(self):
        if self.head:
            self.head = self.head.next
        else:
            raise IndexError("Список пуст")

    def pop_back(self):
        if self.head:
            if not self.head.next:
                self.head = None
                return
            current = self.head
            while current.next.next:
                current = current.next
            current.next = None
        else:
            raise IndexError("Список пуст")

    def delete(self, index):
        if index < 0:
            raise IndexError("Недопустимый индекс")
        if index == 0:
            self.pop_front()
            return
        current = self.head
        for i in range(index - 1):
            if current is None:
                raise IndexError("Недопустимый индекс")
            current = current.next
        if current is None or current.next is None:
            raise IndexError("Недопустимый индекс")
        current.next = current.next.next

    def show(self):
        current = self.head
        elements = []
        while current:
            elements.append(str(current.data))
            current = current.next
        print("[" + ", ".join(elements) + "]")

    def get(self, index):
        if index < 0:
            raise IndexError("Недопустимый индекс")
        current = self.head
        for i in range(index):
            if current is None:
                raise IndexError("Недопустимый индекс")
            current = current.next
        if current is None:
            raise IndexError("Недопустимый индекс")
        return current.data

    def reverse(self):
        prev = None
        current = self.head
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        self.head = prev

    def delete_even(self):
        curr = self.head
        i = 0
        while curr:
            if curr.data % 2 == 0:
                self.delete(i)
            else:
                i += 1
            curr = curr.next

    def unique_count(self):
        unique = []
        curr = self.head
        while curr:
            if curr.data not in unique:
                unique.append(curr.data)
            curr = curr.next
        return len(unique)

# Тесты


linked_list = LinkedList()

linked_list.push_back(1)
print("добавляем 1 в конец")
linked_list.show()

linked_list.push_front(2)
print("\nдобавляем 2 в начало")
linked_list.show()

linked_list.insert(1, 3)
print("\nдобавляем 3 по индексу 1")
linked_list.show()

linked_list.insert(2, 7)
print("\nдобавляем 7 по индексу 2")
linked_list.show()

linked_list.reverse()
print("\nреверс")
linked_list.show()

a = linked_list.get(2)
print("\nпросмотр по индексу 2")
print(a)

linked_list.pop_front()
print("\nудаление элемента из начала")
linked_list.show()

linked_list.pop_back()
print("\nудаление элемента из конца")
linked_list.show()

linked_list.delete(1)
print("\nудаление элемента с индексом 1")
linked_list.show()

linked_list.delete(0)
print("\nудаление элемента с индексом 0")
linked_list.show()

print("\nпопытка удаления элемента из пустого списка")
try:
    linked_list.pop_back()
except IndexError as e:
    print("Ошибка:", e)

for i in range(10):
    linked_list.push_back(i)
    i += 1
linked_list.push_front(1)
linked_list.push_front(1)
linked_list.push_back(9)
print("\nсписок до удаления четных чисел")
linked_list.show()
linked_list.delete_even()
print("список после удаления четных чисел")
linked_list.show()

print("\nколичество уникальных элементов:", linked_list.unique_count())