def reverseList(inputList):
    inputList.reverse()
    for e in inputList:
        if type(e) == type([]):
            e.reverse()
    return inputList

l = [[1, 2], [3, 4], [5, 6, 7]]
l = reverseList(l)
print(l)
