class Deque(object):

    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []
    
    def addFront(self,item):
        self.items.append(item)

    def addRear(self,item):
        self.items.insert(0,item)

    def removeFront(self):
        return self.items.pop()

    def removeRead(self):
        return self.items.pop(0)

    def size(self):
        return len(self.items)
    
d = Deque()
print(d.size())
d.addFront('hello')
d.addFront('yo')
d.addRear('behind')
print(d.items)
print(d.size())
d.removeFront()
print(d.items)
print(d.size())
