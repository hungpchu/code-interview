if __name__ == '__main__':
    s = raw_input()
    
    isNUM = False
    isAlpha = False
    isDigit = False
    islower = False
    isUpper = False
    
    Exist1 = False
    Exist2 =False
    Exist3 = False
    Exist4 = False
    Exist5 =False
    for i in range(len(s)):
        if (s[i].isalnum() and Exist1 == False):
            isNUM = True
            Exist1 = True
            
        if (s[i].isalpha() and Exist2 == False):
            isAlpha = True
            Exist2 = True
            
        if (s[i].isdigit() and Exist3 == False):
            isDigit = True
            Exist3 = True
            
        if (s[i].islower() and Exist4 == False):
            islower = True
            Exist4 = True
    
        if (s[i].isupper() and Exist5 == False):
            isUpper = True
            Exist5 = True
    
    print isNUM
    print isAlpha
    print isDigit
    print islower
    print isUpper



