array = [1,2,4,4]

sum = 8


def isSum(array,sum):
    isSum = False
    highIndex = len(array) - 1
    lowIndex = 0
    for i in range(len(array)):
        if (array[highIndex] + array[lowIndex] == sum):
            isSum = True
        elif (array[highIndex] + array[lowIndex] > sum):
            highIndex = highIndex - 1
        elif (array[highIndex] + array[lowIndex] < sum):
            lowIndex += 1

    return isSum


print ("Result = ",isSum(array,sum))
