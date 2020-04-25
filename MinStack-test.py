"""
Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

push(x) -- Push element x onto stack.
pop() -- Removes the element on top of the stack.
top() -- Get the top element.
getMin() -- Retrieve the minimum element in the stack.

Example:

    MinStack minStack = new MinStack();
    minStack.push(-2);
    minStack.push(0);
    minStack.push(-3);
    minStack.getMin();   --> Returns -3.
    minStack.pop();
    minStack.top();      --> Returns 0.
    minStack.getMin();   --> Returns -2.
"""


class Node:

    def __init__(self, x):
        self.data = x
        self.next = None
        self.prev = None


class MinStack(object):
    min = float('inf')

    def __init__(self):
        self.min = float('inf')
        self.stack = []

    def push(self, x):
        if x <= self.min:
            self.stack.append(self.min)
            self.min = x
        self.stack.append(x)

    def pop(self):
        t = self.stack[-1]
        self.stack.pop()
        if self.min == t:
            self.min = self.stack[-1]
            self.stack.pop()

    def top(self):
        return self.stack[-1]

    def getMin(self):
        return self.min


# Your MinStack object will be instantiated and called as such:
obj = MinStack()
print(obj.push(-2))
print(obj.push(0))
print(obj.push(-1))
print(obj.getMin())
print("----->>>>")

print(obj.top())
# print(obj.pop())
print(obj.getMin())
