def findPair(array,lenArray,hashMap):
    for i in range(lenArray - 1):
        for j in range(i+1,lenArray):
            sum = array[i] + array[j]

            if ( hashMap.get(sum)):
                return True
            else:
                hashMap[sum] = 1
    return False

array = [3,4,7,1,2,9,8]
lenArray = len(array)
hashMap = {}
print(findPair(array, lenArray,hashMap))
