'''
Implement a Queue

* Check if Queue is Empty
* Enqueue
* Dequeue
* Return the size of the Queue
'''
class Queue(object):

    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def enqueue(self,item):
        self.items.insert(0,item)

    def dequeue(self):
        self.items.pop(0)

    def size(self):
        return len(self.items)

# test functions
q = Queue()
print(q.isEmpty())
print(q.size())
