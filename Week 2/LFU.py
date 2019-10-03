class DoublyLinkedList:
        
    @staticmethod
    def createHead(node):
        node.next = node
        node.prev = node

    @staticmethod   
    def insertBetween(node, nextNode, prevNode):
        node.next = nextNode
        node.prev = prevNode
        nextNode.prev = node
        prevNode.next = node 
      
    @staticmethod
    def addNewNodeTo(node, newNode):
        DoublyLinkedList.insertBetween(newNode, node, node.prev)
    
    @staticmethod
    def insertAfter(node, newNode):
        DoublyLinkedList.insertBetween(newNode, node.next, node)

    @staticmethod
    def removeNode(node):
        node.prev.next = node.next
        node.next.prev = node.prev
        node.next = None
        node.prev = None

        return node
    
    @staticmethod
    def isEmpty(node):
        if (node.next == node.prev == node):
            return True
        else:
            return False

        
class FrequencyNode:

    def __init__(self, frequency):
        self.frequency = frequency
        self.next = None
        self.prev = None
        self.head = Cache(-1, -1, self)
        DoublyLinkedList.createHead(self.head)

    def pop(self):
        head = self.head
        retNode = DoublyLinkedList.removeNode(head.next)
        if (DoublyLinkedList.isEmpty(head)):
            DoublyLinkedList.removeNode(self)

        return retNode

class Cache:

    def __init__(self, key, value, frequencyNode):
        self.prev = self.next = None
        self.frequencyNode = frequencyNode
        self.value = value
        self.key = key
    
    def updateFrequency(self):
        tempFNode = self.frequencyNode
        newFrequencyNode = None

        if (DoublyLinkedList.isEmpty(tempFNode) or tempFNode.next.frequency != tempFNode.frequency + 1):
            newFrequencyNode = FrequencyNode(self.frequencyNode.frequency + 1)
            DoublyLinkedList.insertAfter(tempFNode, newFrequencyNode)
        else:
            newFrequencyNode = tempFNode.next

        self.frequencyNode = newFrequencyNode
        DoublyLinkedList.removeNode(self)
        DoublyLinkedList.addNewNodeTo(newFrequencyNode.head, self)

        if (DoublyLinkedList.isEmpty(tempFNode.head)):
            DoublyLinkedList.removeNode(tempFNode)
            
class LFUC(object):

    def __init__(self, size):
        self.map = {}
        self.size = size
        self.head = FrequencyNode(-1)
        DoublyLinkedList.createHead(self.head)
        
    def get(self, key):
        if (key in self.map):
            curNode = self.map[key]
            curNode.updateFrequency()
            return curNode.value
        else:
             return -1
        
    def put(self, key, value):
        if (key in self.map):
            curNode = self.map[key]
            curNode.value = value
            curNode.updateFrequency()
        else:
            if (len(self.map) >= self.size):
                del self.map[self.head.next.pop().key]

            frequencyNode = FrequencyNode(0)
            cacheNode = Cache(key, value, frequencyNode)
            DoublyLinkedList.addNewNodeTo(frequencyNode.head, cacheNode)
            DoublyLinkedList.insertAfter(self.head, frequencyNode)
            self.map[key] = cacheNode
            cacheNode.updateFrequency()

cache = LFUC(2)
cache.put(1, 1)
cache.put(2, 2)
cache.get(1)      
cache.put(3, 3)    
cache.get(2)       
cache.get(3)       
cache.put(4, 4)  
cache.get(1)       
cache.get(3)       
cache.get(4)       
