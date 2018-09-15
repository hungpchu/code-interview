def isSubsetSum(array, sumValue):
    bol = False
    for i in range(len(array)):
        j = i + 1
        for j  in range(len(array)):
            if (array[i] + array[j] == sumValue or array[i] == sumValue or array[j] == sumValue):
                bol = True

    return bol


array = [3, 34, 4, 12, 5, 2]
sumValue = 34 

print isSubsetSum(array, sumValue)
