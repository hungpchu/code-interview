charStack = []
intStack = []
string = ""
result = ""
final = ""
number1 = ""

s= "10[leetcode]11[e]"
# s= "3[a]2[bc]"
# s= "2[abc]3[cd]ef"

for val in s:
    if (val.isdigit()):
        number1 += val
    elif (val == "]"):
        number = int(intStack.pop())
        openbra = ""
        while ( openbra != "["):
            openbra = charStack.pop()
            if (openbra != "["):
                string += openbra
        result = number * string
        charStack.append(result)
        string = ""
    elif (val == "["):
        intStack.append(number1)
        charStack.append(val)
        number1 = ""
    else:
        charStack.append(val)
        
        
while(len(charStack) > 0):
    final += charStack.pop()
    
print(" final = ", final[::-1])
