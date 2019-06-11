n=int(input())
arr=list(map(int,input().split()))
num=1;
for x in arr:
    num*=x
for x in arr:
    print(num//x,end=" ")
