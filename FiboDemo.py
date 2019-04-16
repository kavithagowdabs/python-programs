#fibonacci
n=int(input("enter num"))
#print(n)
n1=0
n2=0
n3=1
for i in range(1,n):
    n1=n2
    n2=n3
    n3=n1+n2
    print(n1)
