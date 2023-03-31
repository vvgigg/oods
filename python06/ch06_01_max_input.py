def max(a):
    if len(a)==1:
        return a[0]
    elif a[0] < a[1]:
        return max(a[1:])
    else:
        a.pop(1)
        return max(a)
S = list(map(int , input("Enter Input : ").split()))
print("Max : "+str(max(S)))