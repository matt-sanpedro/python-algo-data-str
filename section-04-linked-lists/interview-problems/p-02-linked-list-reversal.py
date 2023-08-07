'''
Linked List Reversal 

Problem Statement:
Write a function to reverse a Linked List in place. 
The function will take in the head of the list as input and return the new head of the list.
'''
class Node(object):

    def __init__(self,value):
        self.value = value
        self.nextnode = None

def reverse(head):
    current = head
    previous = None
    nextnode = None

    while current:
        # copy current nodes next node to variable nextnode
        nextnode = current.nextnode

        # reverse the pointer on next node, 1st time will be None as initialized
        # print('PREVIOUS: {}'.format(previous))
        current.nextnode = previous

        # march one step forward in list
        previous = current
        current = nextnode

    # print(previous)
    return previous

# Create a list of 4 nodes
a = Node(1)
b = Node(2)
c = Node(3)
d = Node(4)

# Set up order a,b,c,d with values 1,2,3,4
a.nextnode = b
b.nextnode = c
c.nextnode = d

print(a.nextnode.value)
print(b.nextnode.value)
print(c.nextnode.value)
# print(d.nextnode.value)
reverse(a)
print(d.nextnode.value)
print(c.nextnode.value)
print(b.nextnode.value)
# print(a.nextnode.value)
