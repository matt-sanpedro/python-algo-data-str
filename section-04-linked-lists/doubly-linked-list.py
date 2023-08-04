class DoublyLinkedListNode(object):

    def __init__(self,value):
        self.value = value
        self.nextNode = None
        self.prevNode = None

a = DoublyLinkedListNode(1)
b = DoublyLinkedListNode(2)
c = DoublyLinkedListNode(3)

a.nextNode = b
b.prevNode = a
b.nextNode = c
c.prevNode = b

# # can create circular list
# c.nextNode = a
# a.prevNode = c
