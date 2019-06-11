m,n=map(int,input().split())
mat=[[] for _ in range(m)]
for i in range(n-1):
    a=list(map(int,input().split()))
    if(a.count(0)>0):
        for j in range(len(a)):
            print("0",end=" ")
        print()
    else:
        print(*a,end="")
