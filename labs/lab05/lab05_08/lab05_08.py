class Stack:
    def __init__(self):
        self.__data = []

    def write(self, value):
        self.__data.insert(0, value)

    def is_empty(self):
        return len(self.__data) == 0

    def delete(self):
        if self.is_empty():
            raise Exception("Нечего удалять - стек пустой!")
        else:
            element = self.__data[0]
            self.__data.pop(0)
            return element

    def read_top(self):
        if self.is_empty():
            raise Exception("Нечего считывать - стек пустой!")
        return self.__data[0]

    def clear(self):
        self.__data.clear()

    def display(self):
        print(self.__data)


print("Задание 1.")

stack = Stack()
print("Введите строку из скобочек")
string = input()
for i in range(len(string)):
    if string[i] == '(' or string[i] == '[' or string[i] == '{':
        stack.write(string[i])
    elif string[i] == ')' or string[i] == ']' or string[i] == '}':
        if not stack.is_empty() and stack.read_top() == '(' and string[i] == ')':
            stack.delete()
        elif not stack.is_empty() and stack.read_top() == '[' and string[i] == ']':
            stack.delete()
        elif not stack.is_empty() and stack.read_top() == '{' and string[i] == '}':
            stack.delete()
        else:
            raise Exception("Скобки не совпадают!")
print("Задание выполнено! Стек выглядел так:")
stack.display()
stack.clear()


print("Задание 2.")
print("Введите строку из цифр и арифметических знаков, например: 574+3*+")
string = input()
for i in range(len(string)):
    if string[i].isdigit():
        stack.write(string[i])
    elif string[i] in '+-*/':
        if not stack.is_empty():
            if (stack.read_top()).isdigit():
                item1 = int(stack.read_top())
                stack.delete()
        else:
            raise Exception("Нет достаточного количества чисел для проведения операции")

        if not stack.is_empty():
            if (stack.read_top()).isdigit():
                item2 = int(stack.read_top())
                stack.delete()
        else:
            raise Exception("Нет достаточного количества чисел для проведения операции")

        if string[i] == '+':
            stack.write(str(item1 + item2))
        if string[i] == '-':
            stack.write(str(item1 - item2))
        if string[i] == '*':
            stack.write(str(item1 * item2))
        if string[i] == '/':
            stack.write(str(item1 / item2))

stack.display()
print("Задание выполнено!")
print("Запускаю приложение!")


def main():
    stack = Stack()
    while True:
        print("1: Запись значения в стек")
        print("2: Удаление значения из стека")
        print("3: Просмотр верхнего значения стека")
        print("4: Очистка стека")
        print("5: Просмотр всего стека")
        print("6: Выход")
        try:
            choice = int(input("Выберите действие: "))

            if choice == 1:
                value = input("Введите значение для записи в стек: ")
                stack.write(value)
            elif choice == 2:
                print("Удаленное значение: ", stack.delete())
            elif choice == 3:
                print("Верхнее значение стека: ", stack.read_top())
            elif choice == 4:
                stack.clear()
                print("Стек очищен.")
            elif choice == 5:
                print("Весь стек: ")
                stack.display()
            elif choice == 6:
                print("Выход из программы.")
                break
            else:
                print("Неправильный ввод. Попробуйте еще раз.")
        except ValueError:
            print("Ввод должен быть числом. Попробуйте еще раз.")
        except Exception as e:
            print(f"Произошла ошибка: {str(e)}")


if __name__ == "__main__":
    main()