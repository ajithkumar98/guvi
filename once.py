l=int(input())
arr=list(map(int,input().split()))
val=arr[0]
for i in range(1,len(arr)):
    val=val^arr[i]
print(val)
