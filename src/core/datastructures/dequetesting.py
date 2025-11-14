from deque import Deque

dq = Deque[int]()
dq.push_right(1)
dq.push_right(2)
dq.push_right(3)
print("Start:", dq.items)  # [1, 2, 3]

dq.push_left(0)
print("After push_left(0):", dq.items)  # [0, 1, 2, 3]

print("pop_left():", dq.pop_left())   # 0
print("pop_right():", dq.pop_right()) # 3
print("Now:", dq.items)               # [1, 2]

dq.extend([3, 4])
print("After extend([3, 4]):", dq.items)  # [1, 2, 3, 4]

dq.rotate(1)
print("After rotate(1):", dq.items)       # [4, 1, 2, 3]

dq.rotate(-2)
print("After rotate(-2):", dq.items)      # [2, 3, 4, 1]

dq.reverse()
print("After reverse():", dq.items)       # [1, 4, 3, 2]
