'''
Implement a Deque 

* Check if its empty
* Add to both front and rear
* Remove from Front and Rear
* Check the Size

Sample list with definition:

FRONT                   REAR
[a, b, c, ..., x, y, z]
'''
class Deque(object):

    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def addFront(self,item):
        self.items.insert(0,item)

    def removeFront(self):
        self.items.pop(0)

    def addRear(self,item):
        self.items.append(item)

    def removeRear(self):
        self.items.pop()

    
    
d = Deque()
print(d.isEmpty())
d.addFront(1)
d.addFront(2)
d.addFront(3)
print(d.items)
d.removeFront()
print(d.items)
d.addRear(100)
d.addRear(99)
print(d.items)
d.removeRear()
print(d.items)
