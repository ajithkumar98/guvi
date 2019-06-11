n=int(input())
arr1=list()
for x in range(n):
	arr2=list(map(int,input().split()))
	arr1=arr1+arr2
arr1=sorted(arr1)
for x in arr1:
	print(x,end=" ")
