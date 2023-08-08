'''
Linked List Nth to Last Node 

Problem Statement:
Write a function that takes a head node and an integer value **n** and then returns the nth to last node in the linked list. For example, given:
'''
class Node:

    def __init__(self, value):
        self.value = value
        self.nextnode  = None


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


def nth_to_last_node(n, head):
    current = reverse(head)
    # print(current.value)

    for i in range(n-1):
        # value = current.value
        current = current.nextnode
        # print(i)

    return current


def nth_to_last_node2(n, head):
    left_pointer = head
    right_pointer = head

    for i in range(n-1):
        if not right_pointer.nextnode:
            raise LookupError('Error: n is larger than the linked list')
        
        right_pointer = right_pointer.nextnode

    while right_pointer.nextnode:
        left_pointer = left_pointer.nextnode
        right_pointer = right_pointer.nextnode

    return left_pointer


a = Node(1)
b = Node(2)
c = Node(3)
d = Node(4)
e = Node(5)

a.nextnode = b
b.nextnode = c
c.nextnode = d
d.nextnode = e

# This would return the node d with a value of 4, because its the 2nd to last node.
# target_node = nth_to_last_node(2, a)
# print(target_node.value)
target_node2 = nth_to_last_node2(2, a)
print(target_node2.value)
