def calculator(input):
    numStack = list()
    input = list(input)
    numbers = ""
    while(len(input) > 0):
        curChar = input.pop(0)
        if (curChar in "0123456789"):
            numbers = numbers + curChar
        else:
            if (numbers != ""):
                numStack.append(numbers)
                numbers = ""
            if (curChar in "+*"):
                numStack.append(curChar)
            elif(curChar == ")" and len(numStack) != 3):
                nextNum = numStack.pop()
                operator = numStack.pop()
                firstNum = numStack.pop()

                if (operator == "+"):
                    numStack.append(str(int(firstNum) + int(nextNum)))
                if (operator == "*"):
                    numStack.append(str(int(firstNum) * int(nextNum)))
    return numStack.pop()

expr = "(((((((1+2))))*3)))"
print(calculator(expr))

