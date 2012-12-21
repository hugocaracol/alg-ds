class Stack:
    def __init__(self):
        self.top = None

    def push(self, obj):
        node = StackNode(obj)
        if self.top is not None:
            node.next = self.top
            self.top = node
        else:
            self.top = node

    def pop(self):
        if self.top is None:
            return None
        node = self.top
        self.top = self.top.next

        return node.item


class StackNode:
    def __init__(self, item):
        self.item = item
        self.next = None


stack = Stack()  # creates the stack object
stack.push("Plate1")
stack.push("Plate2")
#then we pop them
print stack.pop()  # Plate2
print stack.pop()  # Plate1
