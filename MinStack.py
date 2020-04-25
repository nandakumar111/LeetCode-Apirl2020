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


class MinStack:

    def __init__(self):
        self.head = None
        self.min = []

    def push(self, x: int) -> None:

        if self.head is None:
            self.head = Node(x)
            self.min.append(x)
        else:
            new_node = Node(x)
            self.head.prev = new_node
            new_node.next = self.head
            new_node.prev = None
            self.head = new_node

            self.min.append(x)
            self.min.sort(reverse=True)

    def pop(self) -> None:
        if self.head is None:
            return None
        else:
            temp = self.head.data
            self.head = self.head.next
            # self.head.prev = None

            if temp in self.min:
                self.min.remove(temp)

            return None

    def top(self) -> int:

        return self.head.data

    def getMin(self) -> int:
        print(self.min)
        try:
            return self.min[-1]
        except IndexError:
            return 0


# Your MinStack object will be instantiated and called as such:
obj = MinStack()
print(obj.push(-2))
print(obj.push(0))
print(obj.push(-1))
print(obj.getMin())
print(obj.top())
print(obj.pop())
print(obj.getMin())
