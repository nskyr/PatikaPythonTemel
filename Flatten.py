def Flatten(inputList):
    flattenList = []
    for e in inputList:
        if type(e) != type([]):
            flattenList.append(e)
        else:
            flattenList.extend(Flatten(e))
    return flattenList
    

inputList = [[1, 'a', ['cat'], 2], [[[3]], 'dog'], 4, 5]
inputList=Flatten(inputList)
print(inputList)