
def subArraySum(arr, n, sum): 
	
	curr_sum = arr[0] 
	start = 0

	i = 1
	while i <= n: 
		 
		while curr_sum > sum and start < i-1: 
		
			curr_sum = curr_sum - arr[start] 
			start += 1
			
		if curr_sum == sum: 
			print ("YES") 
			return 1

		if i < n: 
			curr_sum = curr_sum + arr[i] 
		i += 1
 
	print ("NO") 
	return 0


n,m=map(int,input().split())
arr=list(map(int,input().split()))
subArraySum(arr, n, m) 

