# Лабораторная работа 5
## Бинарное дерево поиска (BST)


### Описание задачи
Реализовать бинарное дерево поиска для хранения целых чисел. Каждый узел содержит значение, а также ссылки на левого и правого потомка. Для любого узла все элементы в левом поддереве меньше его значения, а в правом - больше.

---

### Обязательная часть

Реализовать функции:
- `insert(root, value)`: вставить значение в дерево поиска. При необходимости создавать корневой узел.
- `search(root, target)`: найти, содержится ли значение в дереве (возвращать True/False или сам узел).
- `inorder(root)`: вывести значения в порядке возрастания (симметричный обход).

---

### Вариативная часть
3. Подсчитать количество узлов в дереве (`size`).

---

### 1. Реализация BST

```python
class Node:
    def __init__(self, value: int):
        self.value = value
        self.left = None
        self.right = None


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, value: int) -> None:
        if self.root is None:
            self.root = Node(value)
        else:
            self._insert_recursive(self.root, value)

    def _insert_recursive(self, current_node: Node, value: int) -> None:
        if value < current_node.value:
            if current_node.left is None:
                current_node.left = Node(value)
            else:
                self._insert_recursive(current_node.left, value)
        elif value > current_node.value:
            if current_node.right is None:
                current_node.right = Node(value)
            else:
                self._insert_recursive(current_node.right, value)

    def search(self, target: int) -> bool:
        return self._search_recursive(self.root, target)

    def _search_recursive(self, current_node: Node, target: int) -> bool:
        if current_node is None:
            return False
        if target == current_node.value:
            return True
        
        if target < current_node.value:
            return self._search_recursive(current_node.left, target)
        return self._search_recursive(current_node.right, target)

    def inorder(self) -> list:
        result = []
        self._inorder_recursive(self.root, result)
        return result

    def _inorder_recursive(self, current_node: Node, result: list) -> None:
        if current_node:
            self._inorder_recursive(current_node.left, result)
            result.append(current_node.value)
            self._inorder_recursive(current_node.right, result)

    def size(self) -> int:
        return self._size_recursive(self.root)

    def _size_recursive(self, current_node: Node) -> int:
        if current_node is None:
            return 0
        return 1 + self._size_recursive(current_node.left) + self._size_recursive(current_node.right)
```
---

### 2. Проверка работы

```python
if __name__ == "__main__":
    bst = BinarySearchTree()

    # 1. Тест insert
    bst.insert(50)
    bst.insert(30)
    bst.insert(70)
    bst.insert(20)
    bst.insert(40)
    bst.insert(60)
    bst.insert(80)

    #        50
    #       /  \
    #     30    70
    #    /  \  /  \
    #   20  40 60  80

    # 2. Тест inorder
    print("Inorder:", bst.inorder())  

    # 3. Тест search
    print("Searching: 40:", bst.search(40))
    print("Searching 90:", bst.search(90))

    # 4. Тест size
    print("Nodes in tree:", bst.size())
```

### Вывод в консоль
```
Inorder: [20, 30, 40, 50, 60, 70, 80]
Searching: 40: True
Searching 90: False
Nodes in tree: 7
```
