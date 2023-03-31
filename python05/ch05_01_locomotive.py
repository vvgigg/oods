class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self._size = 0
        
    def __str__(self):
        s = ""
        p = self.head
        while(p != None):
            s += str(p.data)
            p = p.next
        return ' <- '.join(s)
        """
        for i in range(self.size()):
            s += str(p.data) + " "
            p = p.next
        return s
        """
    
    
    def size(self):
        return int(self._size)
    
    def isEmpty(self):
        return self._size == 0
    
    def append(self, data):
        p = Node(data)
        if self.isEmpty():
            self.head = p
            self.tail = p
        else:
            self.tail.next = p
            self.tail = p
        self._size += 1
        
    def addHead(self, data):
        p = Node(data)
        if self.isEmpty():
            self.head = p
            self.tail = p
        else:
            p.next = self.head
            self.head = p
        self._size += 1
        
    def insert(self, index, data):
        if index == 0:
            self.addHead(data)
        elif index == self.size():
            self.append(data)
        else:
            p = Node(data)
            q = self.head
            for i in range(index-1):
                q = q.next
            p.next = q.next
            q.next = p
            self._size += 1
              
    def remove(self, data):
        p = self.head
        q = self.head.next
        if str(p.data) == data:
            self.removeHead()
            return 0
        for i in range(1,self.size()):
            if str(q.data) == str(data):
                if i == self.size()-1:
                    self.removeTail()
                else:
                    p.next = q.next
                    self._size -= 1
                    return i
            p = q
            q = q.next
            
    def removeHead(self):
        h = self.head.data
        self.head = self.head.next
        self._size -= 1
        return h
    
    def removeTail(self):
        p = self.head
        for i in range(self.size()-1):
            p = p.next
        t = self.tail.data
        self.tail = p
        self.tail.next = None
        self._size -= 1
        return t
    
    def isIn(self, data):
        p = self.head
        for i in range(self.size()):
            if str(p.data) == str(data):
                return True
            p = p.next
        return False
    
    def search(self, data):
        p = self.head
        for i in range(self.size()):
            if str(p.data) == str(data):
                return i
            p = p.next
        return -1
    
    
l1 = SinglyLinkedList()
l2 = SinglyLinkedList()

print(' *** Locomotive ***')
inp = [int(e) for e in input('Enter Input : ').split()]

for i in inp:
    l1.append(i)
j = 0
for i in inp:
    if i == 0:
        j = 1
    if j == 1:
        l2.append(i)
for i in inp:
    if i == 0:
        break
    l2.append(i)
    
print('Before :',l1)
print('After :',l2)