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

            return self.Q.pop(0)
        else:
            print("Nothing to pop")
            return

def main():
    q = FixedQSize(3)
    l1 = [1,2,3]
    l2 = [4,5,6]
    l3 = [7,8,9]
    
    q.enqueue(l1)
    q.enqueue(l2)
    q.enqueue(l3)

    print(q.Q)
    print(q.poll())
    print(q.Q)
    print(q.poll())
    print(q.Q)
    print(q.poll())


main()