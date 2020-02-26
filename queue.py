"""
This class implements the queue data structure
It organizes data in the First in, First Out manner
"""

class Queue():

    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.insert(0, item)

    def dequeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)

    def peak(self):
        if not self.is_empty():
            return self.items[-1]

    def bottom_queue(self):
        if not self.is_empty():
            return self.items[0]

    def get_queue(self):
        return self.items

customers = Queue()
customers.enqueue('Bob')
customers.enqueue('Phil')
customers.enqueue('Ashley')
print(customers.get_queue())
print('Number of people in line: '+str(customers.size()))
print('Front of the line: '+customers.peak())
print('Back of the line: '+customers.bottom_queue())
print('Line is empty: '+str(customers.is_empty()))

print()

customers.enqueue('Marry')
print(customers.get_queue())
print('Number of people in line: '+str(customers.size()))
print('Front of the line: '+customers.peak())
print('Back of the line: '+customers.bottom_queue())
print('Line is empty: '+str(customers.is_empty()))

print()

customers.dequeue()
print(customers.get_queue())
print('Number of people in line: '+str(customers.size()))
print('Front of the line: '+customers.peak())
print('Back of the line: '+customers.bottom_queue())
print('Line is empty: '+str(customers.is_empty()))