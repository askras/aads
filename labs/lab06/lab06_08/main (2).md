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

## Двоичные деревья поиска (Binary Search Tree)

<!-- #region -->
### Цель работы

Изучение структуры данных «Двоичное дерево поиска», а также основных операций над ним.

### Задания на лабораторную работу

<!-- #region -->
**1.** Реализовать программу, выполняющую стандартный набор операций над  двоичным деревом поиска:
- формирование бинарного дерева;
- обход (прямой, симметричный, обратный) бинарного дерева;
- удаление заданной вершины из бинарного дерева;
- 
- поиск заданной вершины в бинарном дереве (по значению);
- печать бинарного дерева на экран;
- проверка пустоты бинарного дерева;
- определение высоты бинарного дерева.


Требования:
 - дерево должно быть реализовано в виде класса;
 - каждая операция должна быть реализована как метод класса;
 - добавлению/удалению должна предшествовать проверка возможности выполнения этих операций;

**2.** Реализовать приложение, для работы с бинарным деревом поиска, которое реализует следующий набор действий:

 а) инициализация пустого дерева;

 б) организация диалогового цикла с пользователем;

 **3** Реализовать индивидуальные задание.
<!-- #endregion -->

### Индивидуальные задания

**Задание 1.**

8. Написать функцию, которая определяет, является ли бинарное дерево симметричным.

```angular2html
class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert_node(self, value):
        self.root = self._insert_node(self.root, value)

    def _insert_node(self, root, value):
        if root is None:
            return TreeNode(value)
        if value < root.value:
            root.left = self._insert_node(root.left, value)
        elif value > root.value:
            root.right = self._insert_node(root.right, value)
        return root

    def traverse_in_order(self):
        self._traverse_in_order(self.root)

    def _traverse_in_order(self, root):
        if root:
            self._traverse_in_order(root.left)
            print(root.value, end=' ')
            self._traverse_in_order(root.right)

    def traverse_pre_order(self):
        self._traverse_pre_order(self.root)

    def _traverse_pre_order(self, root):
        if root:
            print(root.value, end=' ')
            self._traverse_pre_order(root.left)
            self._traverse_pre_order(root.right)

    def traverse_post_order(self):
        self._traverse_post_order(self.root)

    def _traverse_post_order(self, root):
        if root:
            self._traverse_post_order(root.left)
            self._traverse_post_order(root.right)
            print(root.value, end=' ')
    def delete_node(self, value):
        if not self.search_node(value):
            print(f"Узел с значением {value} не найден.")
            return
        self.root = self._delete_node(self.root, value)

    def _delete_node(self, root, value):
        if root is None:
            return root
        if value < root.value:
            root.left = self._delete_node(root.left, value)
        elif value > root.value:
            root.right = self._delete_node(root.right, value)
        else:
            if root.left is None:
                return root.right
            elif root.right is None:
                return root.left
            root.value = self._find_min(root.right)
            root.right = self._delete_node(root.right, root.value)
        return root
    def search_node(self, value):
        return self._search_node(self.root, value) is not None

    def _search_node(self, root, value):
        if root is None or root.value == value:
            return root
        if value < root.value:
            return self._search_node(root.left, value)
        return self._search_node(root.right, value)

    def print_tree_structure(self):
        self._print_tree_structure(self.root, 0)

    def _print_tree_structure(self, root, level):
        if root is not None:
            self._print_tree_structure(root.right, level + 1)
            print(' ' * 4 * level + '->', root.value)
            self._print_tree_structure(root.left, level + 1)

    def is_empty_tree(self):
        return self.root is None

    def calculate_tree_height(self):
        return self._calculate_tree_height(self.root)

    def _calculate_tree_height(self, root):
        if root is None:
            return 0
        left_height = self._calculate_tree_height(root.left)
        right_height = self._calculate_tree_height(root.right)
        return max(left_height, right_height) + 1

    def is_symmetric(self):
        if self.root is None:
            return True
        return self._is_symmetric(self.root.left, self.root.right)

    def _is_symmetric(self, left_subtree, right_subtree):
        if not left_subtree and not right_subtree:
            return True
        if left_subtree and right_subtree:
            return (left_subtree.value != right_subtree.value) and \
                self._is_symmetric(left_subtree.left, right_subtree.right) and \
                self._is_symmetric(left_subtree.right, right_subtree.left)
        return False

    def _find_min(self, root):
        current = root
        while current.left is not None:
            current = current.left
        return current.value


def print_menu():
    print("\n1. Вставить узел")
    print("2. Удалить узел")
    print("3. Печать дерева")
    print("4. Обход в прямом направлении")
    print("5. Обход в симметричном направлении")
    print("6. Обход в обратном направлении")
    print("7. Симметричный обход")
    print("8. Поиск узла")
    print("9. Высота дерева")
    print("10. Проверка на симметричность")
    print("11. Проверка пустоты дерева")
    print("12. Выход")

def main():
    bst = BinarySearchTree()

    while True:
        print_menu()

        choice = input("Выберите действие (1-12): ")

        if choice == '1':
            value = int(input("Введите значение узла для вставки: "))
            bst.insert_node(value)
        elif choice == '2':
            value = int(input("Введите значение узла для удаления: "))
            bst.delete_node(value)
        elif choice == '3':
            print("Дерево:")
            bst.print_tree_structure()
        elif choice == '4':
            print("Обход в прямом направлении:")
            bst.traverse_pre_order()
        elif choice == '5':
            print("Симметричный обход:")
            bst.traverse_in_order()
        elif choice == '6':
            print("Обход в обратном направлении:")
            bst.traverse_post_order()
        elif choice == '7':
            print("Симметричный обход:")
            bst.traverse_in_order()
        elif choice == '8':
            value = int(input("Введите значение узла для поиска: "))
            result = bst.search_node(value)
            if result:
                print(f"Узел со значением {value} найден.")
            else:
                print(f"Узел со значением {value} не найден.")
        elif choice == '9':
            print("Высота дерева:", bst.calculate_tree_height())
        elif choice == '10':
            if bst.is_symmetric():
                print("Дерево симметрично.")
            else:
                print("Дерево не симметрично.")
        elif choice == '11':
            if bst.is_empty_tree():
                print("Дерево пусто.")
            else:
                print("Дерево не пусто.")
        elif choice == '12':
            print("Выход из программы.")
            break
        else:
            print("Неверный ввод. Пожалуйста, выберите от 1 до 12.")

if __name__ == "__main__":
    main()
```

### Важные замечания


<!-- #region jp-MarkdownHeadingCollapsed=true -->
### Контрольные вопросы

1. С чем связана популярность использования деревьев в программировании?
```angular2html
Деревья являются одной из наиболее эффективных структур данных для хранения и организации информации.
```
2. Можно ли список отнести к деревьям? Ответ обоснуйте.
```angular2html
Нет, список не является деревом. Список - это упорядоченная коллекция элементов, где каждый элемент имеет свой номер или индекс. В списках элементы могут быть связаны друг с другом только на основе их позиции или индекса. Дерево же представляет собой иерархическую структуру данных, состоящую из узлов (вершин) и ребер (связей) между ними. Каждый узел в дереве может иметь родителя и ноль или более потомков. Дерево обеспечивает более сложные и гибкие способы организации данных и связей между ними. Хотя список и дерево могут использоваться для представления и организации данных, они имеют различные свойства и функции, поэтому не могут рассматриваться как одно и то же.
```
3. Какие данные содержат адресные поля элемента бинарного дерева?
```angular2html
Каждый элемент бинарного дерева содержит два адресных поля, которые указывают на его потомков. Эти поля называются "левым потомком" и "правым потомком"
```
4. Что такое дерево, двоичное дерево, поддерево?
```angular2html
Дерево - это иерархическая структура данных, состоящая из вершин (узлов) и ребер (связей) между ними. Каждая вершина может иметь ноль или более потомков, то есть других вершин, которые связаны с ней. Есть одна вершина, из которой начинаются все связи и которая называется корневой вершиной. Каждая вершина может быть связана с одной родительской вершиной, кроме корневой, которая не имеет родителя.
Двоичное дерево - это особый тип дерева, где каждая вершина может иметь не более двух потомков: левый потомок и правый потомок. Левый потомок находится слева от родительской вершины, а правый потомок - справа от нее.
Поддерево - это часть дерева, которая включает вершину и все ее потомки и связи между ними. Вершина, включая всех ее потомков, называется корневой вершиной поддерева. Поддерево может быть любым фрагментом иерархической структуры дерева.
```
5. Как рекурсивно определяется дерево?
```angular2html
Дерево состоит из вершины (корня) и некоторого количества поддеревьев, которые являются деревьями в себе. Поддеревья соединены с корнем вершины. Каждое поддерево определяется таким же рекурсивным правилом.
```
6. Какие основные понятия связываются с деревьями?
```angular2html
Корень (Root): Корень дерева - это вершина, которая служит начальной точкой для всего дерева. Она не имеет родителя и является вершиной самого верхнего уровня иерархии.
Вершина (Node): Вершина (узел) - это элемент дерева, который содержит некоторую информацию (значение) и связан с другими вершинами (потомками или родителями) через ребра.
Ребро (Edge): Ребро - это связь между двумя вершинами в дереве. Ребро может быть направленным или ненаправленным, в зависимости от типа дерева.
Потомок (Child): Потомок - это вершина, которая связана с другой вершиной (родителем) напрямую нижнего уровня. Родителю может соответствовать несколько потомков.
Родитель (Parent): Родитель - это вершина, от которой исходит ребро, связывающее ее с другой вершиной (потомком). Каждая вершина, за исключением корня, может иметь одного родителя.
Потомки (Children): Потомки - это множество вершин, которые связаны с родительской вершиной. У одной вершины может быть любое количество потомков, включая ноль.
Путь (Path): Путь представляет собой последовательность ребер, связывающих вершины в дереве. Он определяет путь от одной вершины к другой.
Глубина (Depth): Глубина дерева - это количество ребер на пути от корневой вершины до конкретной вершины.
```
7. Какие основные операции характерны при использовании деревьев?
```angular2html
Поиск элементов в дереве
Добавление элемента в дерево
Удаление элемента из дерева
Обход дерева.
```
