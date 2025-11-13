""""
@file stack.py
@brief Stack data structure implementation for the game platform backend.

This module defines the Stack class, a simple Last-In-First-Out (LIFO)
data structure used throughout the backend for undo systems,
temporary storage, and algorithmic utilities.

Usage:
    stack = Stack()
    stack.push(10)
    top = stack.peek()
"""

from typing import Generic, TypeVar, List, Optional

T = TypeVar("T")

class Stack(Generic[T]):
    """"
    A generic LIFO (Last-In, First-Out) stack.

    Provides push, pop, peek, and utility operations. Behaves similarly
    to stacks in typical programming textbooks and interview questions.
    """

    def __init__(self) -> None:
        """
        Initialize an empty stack.

        :return: None
        """
        self.items = []


    def push(self, item: T) -> None:
        """
        Pushes a new item onto the stack.

        :param item: The element to add.
        :return: None
        """
        self.items.append(item)

    def pop(self) -> T:
        """
        Remove and return the top item of the stack.

        :raises IndexError: If the stack is empty.
        :return: The most recently pushed item.
        """
        if not self.is_empty():
            return self.items.pop()
        return None

    def peek(self) -> T:
        """
        Return the top item of the stack without removing it.

        :raises IndexError: If the stack is empty.
        :return: The top item.
        """
        if not self.is_empty():
            return self.items[-1]
        return None

    def is_empty(self) -> bool:
        """
        Checks if the stack is empty.

        :return: True if the stack contains no elements, else False.
        """
        return len(self.items) == 0

    def size(self) -> int:
        """
        Return the number of items currently in the stack.

        :return: Interger size of the stack.
        """
        return len(self.items)

    def clear(self) -> None:
        """
        Remove all elements from the stack.

        :return: None
        """
        self.items: list[T] = []