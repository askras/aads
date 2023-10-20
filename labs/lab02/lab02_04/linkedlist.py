class Node:
    def __init__(self, data):
        self.data = data
        self.nextid = None


class LinkedList:
    def __init__(self):
        self.head = None

    def push_front(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            print(self.head)
            return
        else:
            new_node.nextid = self.head
            self.head = new_node

    def pop_front(self):
        copy_head = self.head
        if self.head is None:
            return
        self.head = self.head.nextid

    def print_linkedlist(self): #iterating over a singly linked list
        copy_head = self.head
        while copy_head is not None:
            print(copy_head.data)
            copy_head = copy_head.nextid

    def __str__(self): #iterating over a singly linked list
        copy_head = self.head
        while copy_head is not None:
            print(copy_head.data)
            copy_head = copy_head.nextid

    def push_back(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            copy_head = self.head
            while copy_head.nextid is not None:
                copy_head = copy_head.nextid
            copy_head.nextid = new_node

    def pop_back(self):
        copy_head = self.head
        if self.head is None:
            return
        else:
            while copy_head.nextid.nextid is not None:
                copy_head = copy_head.nextid
            copy_head.nextid = None

    def linkedlist_size(self):
        copy_head = self.head
        size = 0
        while copy_head is not None:
            size += 1
            copy_head = copy_head.nextid
        return size

    def at(self, index):
        if index < 0 or index > self.linkedlist_size():
            index = index + self.linkedlist_size()
            if index < 0 or index > self.linkedlist_size():
                raise ValueError('Index must be positive and lower than LL size')
            else:
                copy_head = self.head
                for at in index:
                    copy_head = copy_head.nextid
                print(copy_head.data)

    def push(self, data, index):
        new_node = Node(data)
        copy_head = self.head
        position = 0
        if position == index:
            self.push_front(data)
        else:
            while copy_head is not None and position + 1 != index:
                position = position + 1
                copy_head = copy_head.nextid

            if copy_head is not None:
                new_node.nextid = copy_head.nextid
                copy_head.nextid = new_node
            else:
                print("Index not present")

    def pop(self, index):
        if self.head is None:
            return

        copy_head = self.head
        position = 0
        if position == index:
            self.pop_front()
        else:
            while copy_head is not None and position + 1 != index:
                position = position + 1
                copy_head = copy_head.nextid

            if copy_head is not None:
                copy_head.nextid = copy_head.nextid.nextid
            else:
                print("Index not present")

    def check_other(self, data):
        copy_head = self.head
        while copy_head is not None:
            if data == copy_head.data:
                return False
            copy_head = copy_head.nextid
        return True

    def max_elem(self):
        copy_head = self.head
        max_elem = copy_head.data
        while copy_head is not None:
            if max_elem < copy_head.data:
                max_elem = copy_head.data
            copy_head = copy_head.nextid
        copy2_head = self.head
        while copy2_head is not None:
            if max_elem == copy2_head.data:
                self.pop_front()
            copy2_head = copy2_head.nextid










