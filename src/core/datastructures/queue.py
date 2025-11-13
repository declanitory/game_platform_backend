""""
@file queue.py
@brief Queue (FIFO)data structure implementation for the game platform backend.

This module defines the Queue class, a First-In-First-Out structure used for
matchmaking, event processing, and other ordered operations in the backend.

Usage:
    q = Queue()
    q.enqueue("player1")
    next_player = q.dequeue
"""
from typing import Generic, TypeVar, List, Optional

T = TypeVar("T")

class Queue(Generic[T]):
    """
    A generic FIFO (First-In, First-Out) queue.

    Provides enqueue, dequeue, peek, and utility operations. Mirrors typical
    queue interfaces found in backend systems and interview problems.
    """
    def __init__(self) -> None:
        """
        Initialize an empty queue.

        :return: None
        """
        self.items: List[T] = []

    def enqueue(self, item: T) -> None:
        """
        Add an item to the back of the queue.

        :param item: Element to insert.
        :return: None
        """
        self.items.append(item)

    def dequeue(self) -> T:
        """
        Remove and return the item at the front of the queue.

        :raises IndexError: If the queue is empty.
        :return: The item at the front.
        """
        if self.is_empty():
            raise IndexError("dequeue from empty queue")
        return self.items.pop(0)
        

    def peek(self) -> T:
        """
        Return the front item without removing it.

        :raises IndexError: If the queue is empty.
        :return: The front item.
        """
        if self.is_empty():
            raise IndexError("peek from empty queue")
        return self.items[0]

    def is_empty(self) -> bool:
        """
        Checks if the queue is empty.

        :return: True if the queue contains no elements, else False.
        """
        return len(self.items) == 0
    
    def size(self) -> int:
        """
        Get the number of items in the queue.

        :return: Queue length.
        """
        return len(self.items)
    
    def clear(self) -> None:
        """
        Remove all items from the queue.

        :return: None
        """
        self.items.clear()