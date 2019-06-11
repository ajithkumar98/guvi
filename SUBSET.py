m,n=map(int,input().split())
arr1=list(map(int,input().split()))
arr2=list(map(int,input().split()))
flag = 0
if(all(x in arr1 for x in arr2)): 
    flag = 1
if(flag==0):
    print("NO")
else:
    print("YES")
