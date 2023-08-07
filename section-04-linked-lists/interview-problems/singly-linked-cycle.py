'''
Singly Linked List Cycle Check 

Problem Statement:
Given a singly linked list, write a function which takes in the first node in a singly linked list and returns a boolean indicating if the linked list contains a "cycle".

A cycle is when a node's next point actually points back to a previous node in the list. This is also sometimes known as a circularly linked list.

Implementation:

'''
class Node(object):

    def __init__(self,value):
        self.value = value
        self.nextnode = None

def cycle_check(node):
    marker1 = node
    marker2 = node

    # go until end of list, ensure that "faster" marker next node is not none (2nd to last)
    while marker2 != None and marker2.nextnode != None:
        marker1 = marker1.nextnode
        marker2 = marker2.nextnode.nextnode

        # condition: markers match
        if marker2 == marker1:
            return True
    
    # condition: marker reached end of list and no match
    return False

# CREATE CYCLE LIST
a = Node(1)
b = Node(2)
c = Node(3)

a.nextnode = b
b.nextnode = c
c.nextnode = a # Cycle Here!
print(cycle_check(a))

# CREATE NON CYCLE LIST
x = Node(1)
y = Node(2)
z = Node(3)

x.nextnode = y
y.nextnode = z 
print(cycle_check(x))
