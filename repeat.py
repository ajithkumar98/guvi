l=int(input())
arr=list(map(int,input().split()))
for i in range(0,len(arr)):
    if(arr.count(arr[i])>1):
        print(arr[i])
        break
