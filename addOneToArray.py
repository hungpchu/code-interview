array = [9,9,9,9]

stringArray = "".join(str(number) for number in array)

number = int(stringArray,10)

number += 1

result = str(number)
finalResult = []


for i in range(len(result)):
    num = int(result[i],10)
    finalResult.append(num)


print(finalResult)

print(array)


