def power(n, p):
    if p == 0:
        return 1
    else :
        return (n*power(n,p-1))
    
n,p = list(map(int , input("Enter Input a b : ").split()))
print (power(n,p))