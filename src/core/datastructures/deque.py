"""
@file deque.py
@brief Deque (double-ended queue) implementation for the game platform backend.

A deque supports insertion and removal from both ends in O(1) time.
Useful for sliding window algorithms, event logs, and flexible queue behavior.

Usage:
    dq = Deque()
    dq.push_right(10)
    dq.push_left(5)
    print(dq.pop_left())   # 5
"""

from typing import Generic, TypeVar, List, Iterable

T = TypeVar("T")

class Deque(Generic[T]):
    """
    A double-ended queue supporting push/pop operations on both sides.

    Methods:
        push_left(item)
        push_right(item)
        pop_left()
        pop_right()
        peek_left()
        peek_right()
        is_empty()
        size()
        clear()
    """

    def __init__(self) -> None:
        """
        Initialize an empty deque.

        :return: None
        """
        self.items: List[T] = []

    def push_left(self, item: T) -> None:
        """
        Insert an item at the left/front of the deque.

        :param item: The item to insert.
        :return: None
        """        
        self.items.insert(0, item)

    def push_right(self, item: T) -> None:
        """
        Insert an item at the right/back of the deque.

        :param item: The item to insert.
        :return: None
        """        
        self.items.append(item)

    def pop_left(self) -> T:
        """
        Remove and return the leftmost item.

        :raises IndexError: If deque is empty.
        :return: Leftmost item.
        """        
        if self.is_empty():
            raise IndexError("pop_left from empty queue")
        return self.items.pop(0)

    def pop_right(self) -> T:
        """
        Remove and return the rightmost item.

        :raises IndexError: If deque is empty.
        :return: Rightmost item.
        """
        if self.is_empty():
            raise IndexError("pop_right from empty queue")
        return self.items.pop(-1)

    def peek_left(self) -> T:
        """
        Return the leftmost item without removing it.

        :raises IndexError: If deque is empty.
        :return: Leftmost item.
        """        
        if self.is_empty():
            raise IndexError("peek_left from empty queue")
        return self.items[0]

    def peek_right(self) -> T:
        """
        Return the rightmost item without removing it.

        :raises IndexError: If deque is empty.
        :return: Rightmost item.
        """
        if self.is_empty():
            raise IndexError("peek_right from empty queue")
        return self.items[-1]

    def is_empty(self) -> bool:
        """
        Check if the deque has no elements.

        :return: True if empty, else False.
        """        
        return len(self.items) == 0

    def size(self) -> int:
        """
        Get number of elements in the deque.

        :return: Size of deque.
        """
        return len(self.items)

    def clear(self) -> None:
        """
        Remove all elements from the deque.

        :return: None
        """
        self.items.clear()

    # extra operations

    def extend(self, items: Iterable[T]) -> None:
        """
        Extend the deque by appending elements from an iterable to the right.

        Example:
            dq.extend([1, 2, 3])  # existing items remain on the left

        :param items: Iterable of elements to append.
        :return: None
        """
        for item in items:
            self.push_right(item)

    def extend_left(self, items: Iterable[T]) -> None:
        """
        Extend the deque by appending elements from an iterable to the left.

        Note:
            The iterable's order is typically preserved such that the last
            element in 'items' becomes the new leftmost element, similar
            to collections.deque.extendleft().

        :param items: Iterable of elements to append on the left.
        :return: None
        """
        for item in items:
            self.push_left(item)

    def rotate(self, k: int = 1) -> None:
        """
        Rotate the deque k steps to the right (positive) or left (negative).

        Example:
            dq = [1, 2, 3, 4]
            dq.rotate(1)   -> [4, 1, 2, 3]
            dq.rotate(-1)  -> [2, 3, 4, 1]

        :param k: Number of steps to rotate. Positive = right, negative = left.
        :return: None
        """
        n = self.size()
        if n == 0:
            return
        
        k = k % n
        if k > 0:
            for _ in range(k):
                value = self.items.pop()
                self.items.insert(0, value)
        elif k < 0:
            for _ in range(-k):
                value = self.items.pop(0)
                self.items.append(value)
        

    def reverse(self) -> None:
        """
        Reverse the elements of the deque in-place.

        Example:
            dq = [1, 2, 3]
            dq.reverse()  -> [3, 2, 1]

        :return: None
        """
        self.items.reverse()