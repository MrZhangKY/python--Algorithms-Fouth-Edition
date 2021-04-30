def BinarySearch(num, numList):
    numList.sort()  #必须是升序的

    if num<numList[0] or num>numList[-1]:
        '''num直接超出范围'''
        return False

    indexMin = 0
    indexMax = len(numList) - 1
    while indexMin <= indexMax:
        middle = (indexMin + indexMax) // 2
        if numList[middle] < num:
            indexMin = middle + 1
        elif numList[middle] > num:
            indexMax = middle - 1
        else:
            return True #找到准确位置，返回True
    return False    #num不在序列中，返回False

if __name__ == '__main__':
    from functools import reduce
    resList = []
    for i in range(20):
        print(i, BinarySearch(i, list(range(10))))
        resList.append(BinarySearch(i, list(range(10))))
    print(reduce(lambda x,y:x and y, resList[:10]))
    print(reduce(lambda x,y:x or y, resList[10:]))