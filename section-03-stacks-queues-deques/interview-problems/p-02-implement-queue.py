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

    