"""
This class implements the stack data structure
It organizes data in the Last in, First Out manner
"""

class Stack():

    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def is_empty(self):
        return self.items == []

    def peak(self):
        if not self.is_empty():
            return self.items[-1]

    def size(self):
        return len(self.items)

    def get_stack(self):
         return self.items

s = Stack()
s.push('A')
s.push('B')
s.push('C')
s.push('D')
print(s.get_stack())
print('Top of Stack: '+s.peak())
print('Size of Stack: '+str(s.size()))

print()

s.pop()
print(s.get_stack())

print()

s.pop()
print(s.get_stack())
print('Top of Stack: '+s.peak())
print('Size of Stack: '+str(s.size()))
print('Stack is Empty: '+str(s.is_empty()))