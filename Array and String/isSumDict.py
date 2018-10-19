array  = [1,2,4,99,96]

sum = 98


dict = {}

def isSum(string,dict, sum):
    # dict = {}
    for value in array:
        print ("dict be4 = ", dict)
        print("dict.get(sum - value) be4 =", dict.get( value))
        print("sum - value =", sum - value)
        if (  sum - value == dict.get(value) and sum - value >= 0 ):
            return True
        dict[sum -  value] =   value
        print("dict.get(value) =", dict.get(value))
        
    print ("dict = ", dict)
        
    return False
    
print("Result = ", isSum(array,dict,sum))
