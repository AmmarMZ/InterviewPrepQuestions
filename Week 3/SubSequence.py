def mergeWords(s1, s2):
    
    mergedArr = [[""] * (len(s2)+1) for i in range(len(s1)+1)]
    for i in range(len(s1)):
        for j in range(len(s2)):
            if (s1[i] == s2[j]):
                mergedArr[i+1][j+1] = mergedArr[i][j] + s1[i]
            else:
                mergedArr[i+1][j+1] = max((mergedArr[i][j+1], mergedArr[i+1][j]))
    
    match = ""
    i = 0
    j = 0
    for curChar in mergedArr[-1][-1]:
        while s1[i] != curChar:
            match += s1[i]
            i += 1
        while s2[j] != curChar:
            match += s2[j]
            j += 1
        match += curChar
        i += 1
        j += 1
    return match + s1[i:] + s2[j:]

def wordReconstruction(arr):
    word = ""
    for item in arr:
        word = mergeWords(item, word)
    return word

        
_list = ["bs3", "wb3", "wba", "as3f"]
_list2 =["af", "ag"]

print(wordReconstruction(_list2))


