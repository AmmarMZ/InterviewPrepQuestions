class FixedQSize:
    def __init__(self, arraySize):
        self.arraySize = arraySize
        self.Q = []
    
    def enqueue(self, value):

        if (isinstance(value, list)):
            if(len(value) == self.arraySize):
                for i in value:
                    if(not isinstance(i, int)):
                        print("Invalid array")
                        return
            else:
                print("Invalid array length")
                return
        else:
            print("Argument must be a list")
        self.Q.append(value)
    
    def poll(self):
        if(len(self.Q) >= 1):
            return self.Q.pop()
        else:
            print("Nothing to pop")
            return

def main():
    q = FixedQSize(5)
    l1 = [1,2,3,4,'a']
    print(l1)
    print(q.Q)
    q.enqueue(l1)
    print(q.Q)
    print(q.poll())
    print(q.Q)

main()