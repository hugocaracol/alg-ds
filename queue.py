class Queue:
    def __init__(self):
        self.head = None
        self.tail = None

    def Enqueue(self, obj):
        node = QueueNode(obj)
        if self.tail is None:
            self.head = node
        else:
            self.tail.next = node
        self.tail = node

    def Dequeue(self):
        if self.head is None:
            return None
        else:
            node = self.head
            if self.head.next is None:
                self.head = None
                self.tail = None
            else:
                self.head = self.head.next

        return node.item


class QueueNode:
    def __init__(self, item):
        self.item = item
        self.next = None


queue = Queue()  # creates the queue object
queue.Enqueue(10)  # enqueue
queue.Enqueue(99)  # enqueue
print queue.Dequeue()  # 10
print queue.Dequeue()  # 99
