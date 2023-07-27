class Queue(object):

    def __init__(self):
        self.items = []
    
    def isEmpty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.insert(0, item)

    def dequeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)
    
q = Queue()

print(q.isEmpty())
q.enqueue(5)
q.enqueue(9)
q.enqueue(7)
q.enqueue(1)
print(q.items)
print(q.dequeue())
print(q.items)
print(q.isEmpty())
print(q.size())
