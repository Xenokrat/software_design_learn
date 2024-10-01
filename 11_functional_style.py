from typing import TypeVar

T = TypeVar("T")

class Stack[T]:
    """
    Иммутабельный стек, в функцональном стиле
    """

    def __init__(self, list_stack: list[T]) -> None:
        self._stack = list_stack

    def empty(self) -> "Stack":
        return Stack([])

    def push(self, value: T) -> "Stack":
        lst = self._stack.copy()
        lst.append(value)
        return Stack(lst)

    def pop(self) -> "Stack":
        if self.size() == 0:
            raise ValueError("Empty Stack")
        lst = self._stack.copy()
        lst.pop()
        return Stack(lst)

    def peek(self) -> T:
        if self.size() <= 0:
            raise ValueError("Empty Stack")
        return self._stack[-1]

    def size(self) -> int:
        return len(self._stack)

