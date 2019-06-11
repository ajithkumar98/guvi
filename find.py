flag=0
n,m=map(int,input().split())
arr=list(map(int,input().split()))
for i in range(0,len(arr)):
    for j in range(i+1,len(arr)):
        if(arr[i]+arr[j]==m):
            print("YES")
            flag=1

if(flag==0):
    print("NO")

