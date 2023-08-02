'''
Implement a Queue - Using Two Stacks

Given the Stack class below, implement a Queue class using **two** stacks! 
Note, this is a "classic" interview problem. Use a Python list data structure as your Stack.

DEFINITIONS:
Stack: addition of new items and removal of existing items always takes place at the same end
Queue: addition of new items happens at one end (rear/back -> enqueue), and the removal of existing items occurs at the other end (front -> dequeue)

IMPLEMENTATION:
Key insight is a stack reverses order, a queue does not.
A sequence of elements pushed on a stack comes back in reversed order when popped.
Thus, two stacks chained together will return elements in the same order.
'''
class Queue2Stacks(object):
    
    def __init__(self):
        self.instack = []
        self.outstack = []

    def enqueue(self,element):
        self.instack.append(element)

    def dequeue(self):
        if len(self.outstack)==0:
            while self.instack:
                self.outstack.append(self.instack.pop())

        return self.outstack.pop()

q = Queue2Stacks()
for i in range(5):
    q.enqueue(i)

q.dequeue()
print(q.instack)
print(q.outstack)
