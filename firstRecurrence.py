string = "BCABA"


dict = {}

def firstRecurrence(string,dict):
    # dict = {}
    for char in string:
        if (dict.get(char) == char):
            return char
        dict[char] = char
        
    return "none"
    
print("Result = ", firstRecurrence(string,dict))
