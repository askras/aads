from linkedlist import LinkedList


list2 = LinkedList()
list2.check_other(4)
new_elem = 0
while True:
        data = input("Вводите через enter")
        if not data:
            break
        else:
            print(data)
            if list2.check_other(data):
                list2.push_back(data)
list2.print_linkedlist()

list2.max_elem()
print('\n')
list2.print_linkedlist()