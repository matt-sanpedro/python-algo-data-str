'''
Implement a Queue - Using Two Stacks

Given the Stack class below, implement a Queue class using **two** stacks! 
Note, this is a "classic" interview problem. Use a Python list data structure as your Stack.

DEFINITIONS
Stack: addition of new items and removal of existing items always takes place at the same end
Queue: addition of new items happens at one end (rear/back -> enqueue), and the removal of existing items occurs at the other end (front -> dequeue)
'''
class Queue2Stacks(object):

    def __init__(self):

        # two stacks
        self.stack1 = []
        self.stack2 = []

    def enqueue(self,element):
        pass

    def dequeue(self):
        pass

    