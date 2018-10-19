s = "[])"

def isValid( s):
        """
        :type s: str
        :rtype: bool
        """
        
        if (s == ""):
            return True
        
        valid = False
        
        openBra = []
        
        closeBra = []

        for c in s:
            if ( c == "}" or c == "]" or c == ")"):
                closeBra.append(c)
            if ( c == "{" or c == "[" or c == "("):
                openBra.append(c)
            elif  ( c == "}" and len(openBra) > 0):
                if (openBra.pop() == "{" ):
                    valid = True
                    closeBra.pop()
                else:
                    valid = False
                    break
            elif  ( c == ")" and len(openBra) > 0):
                if (openBra.pop() == "(" ):
                    valid = True
                    closeBra.pop()
                else:
                    valid = False
                    break
            elif  ( c == "]" and len(openBra) > 0):
                if (openBra.pop() == "[" ):
                    valid = True
                    closeBra.pop()
                else:
                    valid = False
                    break
        if (len(openBra) > 0 or len(closeBra) > 0):
            valid = False

        return valid

print("Result = ", isValid(s))
