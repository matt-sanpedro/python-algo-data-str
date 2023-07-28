'''
# Implement a Stack 

* Check if its empty
* Push a new item
* Pop an item
* Peek at the top item
* Return the size
'''
class Stack(object):

    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def newItem(self,item):
        self.items.append(item)

    def removeItem(self):
        self.items.pop()

    def peek(self):
        return self.items[len(self.items) - 1]
    
    def size(self):
        return len(self.items)


s = Stack()
print(s.isEmpty())
s.newItem(1)
s.newItem(5)
s.newItem(7)
print(s.items)
s.removeItem()
s.newItem(66)
print(s.items)
print(s.peek())
print(s.size())
print(s.isEmpty())
