def findInflectionPoint(arr):
    temp = arr[0]
    for i in range(1,len(arr)):
        if (arr[i] < temp):
            return temp
        temp = arr[i]
    return temp

arr = [0, 1, 2, 8, 45, 67, 89, 100, 321, 98, 47, -6, -200]
arr2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 1]
arr3 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]
print(findInflectionPoint(arr))
print(findInflectionPoint(arr2))
print(findInflectionPoint(arr3))
