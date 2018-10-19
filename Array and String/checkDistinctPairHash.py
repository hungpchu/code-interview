count = {}
array = [1, 2, 3, 4, 5, 5, 5, 5,5,5,5, 6, 7, 8, 9, 1, 9,10,1,1,10, 0,0 , 10]
sum = 10
def checkDuplicatePair(count,array,sum ):
    countPair = 0
    for value in array:
        if(count.get(value)):
            count[value] +=  1
        else:
            count[value] = 1
            
    for value in array:
        if ( count.get(sum - value) ):
            countPair += 1
            print("value = ", value)
            print(" sum - value = ", sum - value)
            count[sum - value] = 0
            count[value] = 0
    
    return countPair


    
print ("Result = ", checkDuplicatePair(count, array, sum))
        
