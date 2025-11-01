def CheckCommonElement(listA,listB):
    setA = set(listA)
    for i in listB:
        if i in setA:
            return True 
    return False 

listA = ['a','b','c','d','e','d']
listB = ['a','9','wf','fwf','ss','ff']
print(f'this is the result {CheckCommonElement(listB,listA)}')
