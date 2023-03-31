class node:
    def __init__(self, data, next = None) :
        self.data = data
        if next is None :
            self.next = None
        else :
            self.next = next
    def __str__(self):
        return str(self.data)

def createList(l=[]):
    n = node(l[0])
    h = n
    for i in range(1, len(l)):
        q = node(l[i])
        n.next = q
        n = q
    return h

def printList(H):
    s = ''
    while H is not None:
        s += str(H) + ' '
        H = H.next
    print(s)

def mergeOrderesList(p,q):
    m = None
    if p.data <= q.data:
        m = node(p.data)
        p = p.next
    else:
        m = node(q.data)
        q = q.next
    h = m
    while p is not None and q is not None:
        if p.data <= q.data:
            m.next = p
            m = p
            p = p.next
        else:
            m.next = q
            m = q
            q = q.next
    while p is not None:
        m.next = p
        m = p
        p = p.next
    while q is not None:
        m.next = q
        m = q
        q = q.next
    return h

L1, L2 = input('Enter 2 Lists : ').split()
L1 = list(map(int, L1.split(',')))
L2 = list(map(int, L2.split(',')))
LL1 = createList(L1)
LL2 = createList(L2)
print('LL1 : ',end='')
printList(LL1)
print('LL2 : ',end='')
printList(LL2)
m = mergeOrderesList(LL1,LL2)
print('Merge Result : ',end='')
printList(m)