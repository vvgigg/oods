
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.previous = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def __str__(self):
        s=''
        t=self.head
        while t!=None:
            s+=str(t.value)
            t=t.next
            if t!=None:s+='->'
        if s=='':
            s+="Empty"
        return s

    def setNode(self,in1,in2):
        t=self.head
        i=0
        while i!=in1:
            t=t.next
            i+=1
        a=t
        t=self.head
        i=0
        while i!=in2:
            t=t.next
            i+=1
        b=t
        a.next=b
        b.previous=a
        print(f"Set node.next complete!, index:value = {in1}:{a.value} -> {in2}:{b.value}")

    def reverse(self):
        if self.isEmpty():
            return "Empty"
        cur, s = self.tail, str(self.tail.value) + " "
        while cur.previous != None:
            s += str(cur.previous.value) + " "
            cur = cur.previous
        return s

    def isEmpty(self):
        return self.head == None

    def append(self, item):
        a = Node(item)
        if self.isEmpty():
            self.head = a
            self.tail = a
        else:
            a.previous = self.tail
            self.tail.next = a
            self.tail=a

    def addHead(self, item):
        a=Node(item)
        if self.isEmpty():
            self.head=a
            self.tail=a
        else:
            self.head.previous = a
            a.next=self.head
            self.head=a

    def insert(self, pos, item):
        a=Node(item)
        t=self.head
        if pos <= self.size() and pos > 0:
            i=0
            while i< pos-1:
                t=t.next
                i+=1
            a.previous = t.previous
            a.next = t
            t.previous.next = a
            t.previous = a
        elif pos == 0 or -1*pos > self.size():
            
            if self.size()!=0:
                t.previous = a
                a.next = t
                self.head = a
            else:
                self.head=a
                self.tail=a
        elif pos < 0:
            t=self.tail
            i=1
            while i<-1*pos:
                t=t.previous
                i+=1
            a.previous=t.previous
            t.previous.next = a
            a.next = t
            t.previous = a 
        else:
            a.previous = self.tail
            self.tail.next = a
            self.tail = a

    def search(self, item):
        t=self.head
        while t!=None:
            if t.value==item:
                return "Found"
            t=t.next
        return "Not Found"

    def index(self, item):
        t=self.head
        i=0
        while t!=None:
            if t.value == item:
                return i
            t=t.next
            i+=1
        return -1
        
    def size(self):
        sum=0
        head=self.head
        while head!=None:
            sum+=1
            head=head.next
        return sum

    def pop(self, pos):
        t=self.head
        if pos<0 or pos>=self.size():
            return "Out of Range"
        else:
            i=0
            while i<pos:
                t=t.next
                i+=1
            if self.size()==1:
                self.head=None
                self.previous=None
            elif i==0:
                self.head = t.next
                self.head.previous = None
            elif i==self.size()-1:
                self.tail = t.previous
                self.tail.next = None
            else:
                t.next.previous = t.previous
                t.previous.next = t.next
            return "Success"
    
    def checkLoop(self):
        s=set()
        t=self.head
        while t:
            if t in s:
                return True
            s.add(t)
            t=t.next
        return False
        
L = LinkedList()
inp = input("Enter input : ").split(",")
j=0
for i in inp:
    if i[0] == 'A':
        L.append(i[2:])
        print(L)
    elif i[0] == 'S':
        if L.isEmpty():
            print("Error! {list is empty}")
        elif L.size()-1>=int(i[2]) and L.size()-1>=int(i[4]):
            if int(i[2])<int(i[4]):
                L.setNode(int(i[2]),int(i[4]))
            elif int(i[2])>=int(i[4]):
                L.setNode(int(i[2]),int(i[4]))
        elif int(i[2]) > L.size()-1:
            print("Error! {index not in length}: " + i[2])
        elif int(i[4]) > L.size()-1:
            print(f"index not in length, append : {i[4]}")
            L.append(int(i[4]))
print("Found Loop" if L.checkLoop() else "No Loop")
if L.checkLoop():
    pass
else:
    print(L)