l=int(input())
arr=list(map(int,input().split()))
l1=len(arr)
unique=list(set(arr))
l2=len(unique)
if(l1==l2):
    print("unique")
else:
    unique=sorted(unique);
    for i in range(0,len(unique)):
        if(arr.count(unique[i])>1):
            print(unique[i],end=" ")
        
