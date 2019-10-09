class Node:
	def __init__(self, data):
		self.data = data
		self.left = None
		self.right = None

def addNode(inOrder, preOrder, start, end):

	if (start > end):
		return

	tempNode = Node(preOrder[addNode.curIndex])
	addNode.curIndex += 1

	if (start == end):
		return tempNode

	idx = findIndex(inOrder, start, end, tempNode.data)

	tempNode.left = addNode(inOrder, preOrder, start, idx - 1)
	tempNode.right = addNode(inOrder, preOrder, idx + 1, end)

	return tempNode

def findIndex(arr, start, end, value):
	for i in range(start, end + 1):
		if (arr[i] == value):
			return i

def reconstruction(preOrder, inOrder):
	addNode.curIndex = 0
	root = addNode(inOrder, preOrder, 0, len(inOrder) - 1) 
	return root

preOrder = "MLZCWJEOK"
inOrder = "ZCLJWMEKO"
reconstruction(preOrder,inOrder)
