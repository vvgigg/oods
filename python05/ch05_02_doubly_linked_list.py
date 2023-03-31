class DoublyLinkedList :
    class Node :
        def __init__(self,data,prev = None,next = None) :
            self.data = data
            if prev is None :
                self.prev = None
            else :
                self.prev = prev
            if next is None :
                self.next = None
            else :
                self.next = next
        
    def __init__(self):                
            self.dummy = self.Node(None,None,None)
            self.dummy.next = self.dummy.prev = self.dummy
            self.size = 0
            
    def __str__(self):
        s = 'linked list : '
        p = self.dummy.next
        for i in range(len(self)-1) :
            s += str(p.data) + '->'
            p = p.next
        s += str(p.data)
        return s  

    def __len__(self) :
        return self.size
        
    def isEmpty(self) :
        return self.size == 0
    
    def indexOf(self,data) :
        q = self.dummy.next
        for i in range(len(self)) :
            if q.data == data :
                return i
            q = q.next
        return -1
    
    def isIn(self,data) :
        return self.indexOf(data) >= 0
    
    def nodeAt(self,i) :
        p = self.dummy
        for j in range(-1,i) :
            p = p.next
        return p
    def str_reverse(self):
        s = 'reverse : '
        p = self.nodeAt(len(self)-1)
        for i in range(len(self)-1) :
            s += str(p.data) + '->'
            p = p.prev
        s += str(p.data)
        return s 
    def add_before(self,q,data) :
        p = q.prev
        x = self.Node(data,p,q)
        p.next = q.prev = x
        self.size += 1
        
    def append(self,data) :
        self.add_before(self.nodeAt(len(self)),data)
  
    def removeNode(self,q) :   
        p = q.prev
        x = q.next
        p.next = x
        x.prev = p
        self.size -= 1
     
        
    def delete(self,i) :
        self.removeNode(self.nodeAt(i))

l2 = DoublyLinkedList()
lls = input("Enter Input : ").replace(', ',',')
ls = lls.split(',')
for i in ls :
    t= i.split(' ')
    if t[0] == 'A':
        l2.append(t[1])
    elif t[0] == 'Ab':
        l2.add_before(l2.nodeAt(0),t[1])
    elif t[0] == 'I':
        tx = t[1].split(":")
        if int(tx[0])==0:
            print(f'index = {tx[0]} and data = {tx[1]}')
            l2.add_before(l2.nodeAt(int(tx[0])),tx[1])
        elif int(tx[0])<0 or int(tx[0])>len(l2) :
            print("Data cannot be added")
        else :
            print(f'index = {tx[0]} and data = {tx[1]}')
            l2.add_before(l2.nodeAt(int(tx[0])),tx[1])
    elif t[0] == 'R':
        if not l2.isIn(t[1]):
            print("Not Found!")
        else:
            for i in range(len(l2)):
             if l2.nodeAt(i).data == t[1]:
                print(f'removed : {int(t[1])} from index : {i}')
                l2.delete(i)
                break
    if(len(l2)==0):
        print('linked list : ')
        print('reverse : ')
    else :
        print(l2)
        print(str(l2.str_reverse()))