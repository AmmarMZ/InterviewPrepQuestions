def longestAlphaString(input):
	# assuming input is validated beforehand
	temp = input[0]
	output = input[0]
	
	for i in range(len(input)-1):
		if input[i]<= input[i+1]:
			temp = temp + input[i+1]
			if len(temp) > len(output):
				output = temp           
		else:
			temp = input[i+1]

	print("Output: :" + output)
	
longestAlphaString("zyma")