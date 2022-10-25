def minSwap(arr, n, k) : 

	count = 0
	for i in range(n) : 
		if (arr[i] <= k) : 
			count = count + 1

	bad = 0
	for i in range(count) : 
		if (arr[i] > k) : 
			bad = bad + 1

	ans = bad 
	j = count 
	for i in range(n) : 
		
		if(j == n) : 
			break

		if (arr[i] > k) : 
			bad = bad - 1

		if (arr[j] > k) : 
			bad = bad + 1
      
		ans = min(ans, bad) 

		j = j + 1

	return ans 

arr = [2, 1, 5, 6, 3] 
n = len(arr) 
k = 3
print (minSwap(arr, n, k)) 

arr1 = [2, 7, 9, 5, 8, 7, 4] 
n = len(arr1) 
k = 5
print (minSwap(arr1, n, k)) 

