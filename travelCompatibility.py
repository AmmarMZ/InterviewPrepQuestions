def travelCompatibility(myInput, friendsInput):

	maxMatches = 0
	matchedIndex = -1
	index = 0
	
	for input in friendsInput:
		temp = set(myInput).intersection(input)
		
		if (len(temp) > maxMatches):
			maxMatches = len(temp)
			matchedIndex = index
		index += 1
		
	return matchedIndex

index = travelCompatibility(["YYZ","JFK","SFO"], [["YXU", "JFaK"],["SFsO", "BOS", "JsFK"],["LGA"]])

print("Output: " , index)