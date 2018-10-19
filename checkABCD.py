count = {}
string = "DBCABA"
def checkABCD(count,string):
    for char in string:
        if(count.get(char) ):
            return char
        count[char] = 1
    return 'none'
    
    
    
print (checkABCD(count, string))
        
