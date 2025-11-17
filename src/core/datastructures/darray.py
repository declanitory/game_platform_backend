"""
@file darray.py
@brief Dynamic array (resizable array) implementation for backend fundamentals.

A dynamic array grows automatically when capacity is reached.
Supports amortized O(1) append operations like Python's built-in list.

Usage:
    arr = DynamicArray()
    arr.append(10)
    arr.append(20)
    print(arr.get(0))  # 10
"""

from typing import Generic, TypeVar, List, Optional

T = TypeVar("T")

class DynamicArray(Generic[T]):
    """
    A resizeable array supporting automatic growth.

    Internal structure:
        - self._array: underlying fixed-size array
        - self._size: number of elements currently stored
        - self._capacity: total allocated slots

    Methods:
        append(item)
        insert(index, item)
        pop()
        get(index)
        set(index, value)
        size()
        capacity()
        clear()
    """

    def __init__(self, initial_capacity: int = 4) -> None:
        """
        Initialize the dynamic array.

        :param initial_capacity: Starting capacity (default 4).
        """
        pass

    def _resize(self, new_capacity: int) -> None:
        """
        Resize the underlying array to a new capacity.

        :param new_capacity: The new capacity for the array.
        """
        pass

    def append(self, item: T) -> None:
        """
        Add an item to the end of the array.

        :param item: Element to append.
        """        
        pass

    def insert(self, index: int, item: T) -> None:
        """
        Insert an element at a specific index.

        :param index: Position to insert.
        :param item: Item to insert.
        :raises IndexError: If index is out of range.
        """        
        pass

    def pop(self) -> T:
        """
        Remove and return the last element.

        :raises IndexError: If array is empty.
        """
        pass  # TODO: return last element, shrink if needed

    def get(self, index: int) -> T:
        """
        Retrieve the element at a given index.

        :param index: Position to access.
        :raises IndexError: If index is out of bounds.
        """
        pass  # TODO: bounds check, return element

    def set(self, index: int, value: T) -> None:
        """
        Set the element at the given index to a new value.

        :param index: Position to update.
        :param value: New value.
        :raises IndexError: If index is out of bounds.
        """
        pass

    def size(self) -> int:
        """
        Get the number of stored elements.

        :return: Size of the array.
        """
        pass

    def capacity(self) -> int:
        """
        Get the current capacity of the underlying array.

        :return: Internal array capacity.
        """
        pass

    def clear(self) -> None:
        """
        Remove all elements from the array.

        :return: None
        """
        pass