l=int(input())
arr=list(map(int,input().split()))
flag=0
for i in range(0,len(arr)):
    if(arr.count(arr[i])>1):
        print(arr[i])
        flag=1
        break
if flag==0:
    print("unique")
