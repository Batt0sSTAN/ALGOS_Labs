class Stack:
    def __init__(self):
        self.stack = []

    def is_empty(self):
        return not self.stack

    def push(self, data):
        self.stack.append(data)

    def pop(self):
        if not self.is_empty():
            return self.stack.pop()
        return None

    def peek(self):
        if not self.is_empty():
            return self.stack[-1]
        return None

    def size(self):
        return len(self.stack)

    def print_stack(self):
        print(self.stack)


class QueueWithTwoStacks:
    def __init__(self):
        self.stack_in = Stack()
        self.stack_out = Stack()

    def enqueue(self, x: any) -> None:
        self.stack_in.push(x)

    def _move_elements(self) -> None:
        if self.stack_out.is_empty():
            while not self.stack_in.is_empty():
                self.stack_out.push(self.stack_in.pop())

    def dequeue(self) -> any:
        if self.isEmpty():
            return None
        
        self._move_elements()
        return self.stack_out.pop()

    def front(self) -> any:
        if self.isEmpty():
            return None
        
        self._move_elements()
        return self.stack_out.peek()

    def isEmpty(self) -> bool:
        return self.stack_in.is_empty() and self.stack_out.is_empty()

if __name__ == "__main__":
    queue = QueueWithTwoStacks()

    print(queue.isEmpty())

    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)

    print(queue.isEmpty())
    print(queue.front())    # Выведет: 1 (первым добавили 1)

    # Извлекаем элементы
    print(queue.dequeue())  # Извлечет 1
    print(queue.dequeue())  # Извлечет 2

    queue.enqueue(4)

    print(queue.dequeue())  # Извлечет 3
    print(queue.dequeue())  # Извлечет 4
    print(queue.isEmpty())  # Очередь пустая