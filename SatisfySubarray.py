from itertools import chain, combinations

def satisfySubarrays(input, k):
	# assuming params are validated beforehand and 
	# input does not have duplicate entries
	
	#input = [i % 2 for i in input]
	powerset = list(powersetOf(input))
	numOfSubArrays = 0;
	
	start =  True
	if (k == 0):
		# in this case we want to include the null set
		start = False
	
	for set in powerset:
		# to skip null set
		if (start == True):
			start = False
			continue
		# ignore sets smaller than k
		if (len(set) < k):
			continue
		# '0' out all non odd numbers
		# tempSet used to show which sets satisfy
		tempSet = set
		set = [i % 2 for i in set]
		# take the sum of the set
		# since all odd numbers will have been reduced to 1
		# and all even numbers are 0 the sum gives us the number
		# of odd  
		tSum = sum(set)
	
		if (tSum == k):
			print(tempSet)
			numOfSubArrays += 1
	
	return numOfSubArrays
		
	
# gets powerset of input array
# https://stackoverflow.com/questions/1482308/how-to-get-all-subsets-of-a-set-powerset/54288550
def powersetOf(iterable):
    "powerset([1,2,3]) --> () (1,) (2,) (3,) (1,2) (1,3) (2,3) (1,2,3)"
    s = list(iterable)
    return chain.from_iterable(combinations(s, r) for r in range(len(s)+1))
	
print("Output : ",satisfySubarrays([1,2,3,4,5], 2))