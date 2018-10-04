array = [1, 7, 5, 9, 2, 12, 3]
diff = 2

dict = {}

def differ(array,dict,diff):
    count = 0
    
    for value in array:
        dict[value] = value
    print ("dict = ", dict)
    
    for value in array:
 
        if (dict.get(value + diff)   ):
            print("value = 1st", value)
            print(" dict.get(value + diff) trong 1st = ", dict.get(value + diff ))
            dict[value + diff] = 0
       
            count += 1
        elif(dict.get(value - diff)):
            print("value  trong 2nd = ", value)
            print(" dict.get(value - diff) = trong 2nd ", dict.get(value - diff ))
            dict[value - diff] = 0
            count += 1
            
        
    return count
    
print("Result = ", differ(array,dict,diff))
