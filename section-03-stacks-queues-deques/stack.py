class Stack(object):

    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []
    
    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        last_index = len(self.items)-1
        return self.items[last_index]

    def size(self):
        return len(self.items)

    
s = Stack()
print(s.isEmpty())
s.push(5)
s.push(8)
print(s.peek())
print(s.size())
s.pop()
s.pop()
print(s.isEmpty())
