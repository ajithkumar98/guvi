l=int(input())
arr=list(map(int,input().split()))
arr=sorted(arr,reverse=True)
num=0
for i in range(0,len(arr)):
    num=(num*10)+arr[i]
print(num)
