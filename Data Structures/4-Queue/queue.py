#FIFO Pricip, First in first Out

from collections import deque

q = deque()

queue = deque(["Python",54,101.99,True] )

queue.append(3)
print(queue)

queue.pop()
print(queue)

# If i use list and pop an element, all of other elements slide to the left side, however with queue just the pointers of the beginning points now the next element.
# Because of that the adding and deleting an element from queue works faster.

print (not queue) #full or empty

print(queue.count("Python"))
print(queue.count("python"))
print(len(queue))