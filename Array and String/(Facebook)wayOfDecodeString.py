#print("Please input :")
#data =  input()
data = "122211"
# k = last k letter of string
def help(data, k ):
    # if string only has 1 letter -> num way = 1
    if ( k == 0 ):
        return 1
    start = len(data) - k
    if (data[start] == '0'):
        return 0 
    # recursively call helper to find way for last k - 1 letter
    result  = help(data, k - 1)
    # if last k letter still > 2 and first 2 letter of data string <= 26
    if ( k >= 2 and int(data[start: start + 2]) < 26):
        result += help(data, k - 2)
    return result
    
def num_way(data):
    return help(data,len(data))
    
print("Result = ", help(data,len(data)))
    
