def count_substring(string, sub_string):
    count = 0
    length = 0
    result = 0
    if ( len(string) < 1 or len(string) > 200):
        print(exit)
        
    txtLen = len(string)
    patLen = len(sub_string)
    
    # print "hung"
    
   
    
    for i in range(txtLen):
        # print (" i = ngaoai j", i)
        if (string[i] == sub_string[0] ):
            match = True
            count = 1
            if ( patLen != 1):
                j = 1
                while(j < patLen and i + j < txtLen):
                    if (string[i + j] != sub_string[j] ):
                        match = False
                        break
                    if (match):
                        count += 1
                    j += 1
                    # print (" i = trong j", i)
            if ( count == patLen):
                # print("count / pat = ", count/patLen)
                # print (" i trong count == patLen  = ", i)
                result += count/patLen
                    
            
            elif ( patLen == 1 ):
                # print (" i trong else = ", i)
                result += 1
            
    
                           
        
    return result   



string = "ABCDCDCDCDCDCDCDCDC"
sub_string = "CDC"

print( "Number of Sub_string = ",count_substring(string, sub_string))
