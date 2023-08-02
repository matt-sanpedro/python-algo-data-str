'''
Implement a Singly Linked List

PROS:
- linked lists have constant-time insertions and deletions in any position
- in contrast to arrays, array takes O(n) time to do same thing
- linked lists can continue to expand withour having to specify their size ahead of time

CONS:
- to access element in linked list, take O(k) time from head to kth element
- in contrast to arrays, arrays have constant time operation to access elements
'''
class Node(object):

    def __init__(self,value):
        self.value = value 
        self.nextNode = None

a = Node(1)
b = Node(2)
c = Node(3)

a.nextNode = b
b.nextNode = c

print(a.nextNode.value)