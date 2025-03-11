#LIFO Princip Last in First Out

stack = []
stack.append("a")
stack.pop()
print(stack)

stack.append("a")
stack.append("b")
stack.append("c")
stack.append("d")
stack.append("e")
stack.append("f")
print(stack)

stack.pop()
print(stack)

stack.pop()
stack.pop()

print(stack)

print(stack[-1])

print(not stack)

print(len(stack))

from collections import deque

stack2 = deque()


from queue import LifoQueue

stack3 = LifoQueue(maxsize = 3)

stack3.put("a")
stack3.put("b")
stack3.put("c")
stack3.put("d")

stack3.get()
stack3.get()

print(stack3.get())