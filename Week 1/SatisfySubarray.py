from itertools import chain, combinations

def satisfySubarrays(input, k):
	# assuming params are validated beforehand and 
	# input does not have duplicate entries
	
	kToComplete = k
	numOfSubs = 0
	
	
	for i in range(len(input)):
		kToComplete = k
		if (i%2 != 0):
			kToComplete -= 1
			
		for j in range(i, len(input)):
			# if moving value is odd
			if (j%2 != 0):
				kToComplete -=1
			if (kToComplete == 0):
				numOfSubs += 1
				kToComplete = 1
				
	return numOfSubs
				
				
num = satisfySubarrays([1,2,3,4,5], 2)	
print(num)	
			