count = {}
string = "ABCCC"
def checkDuplicate(count,string):
    for char in string:
        if(count.get(char)):
            print("char sau = ", char)
            count[char] +=  1
        else:
            print("char b4 = ", char)
            count[char] = 1
    return count
  
def check1stNonRecur(count,string):
    countR = 0
    for char in string:
        if(count.get(char)):
            count[char] +=  1
        else:
            count[char] = 1
    for char in string:
        if (count.get(char) == 1):
            return char
    
       
    return count


    
print ("Result = ", check1stNonRecur(count, string))
