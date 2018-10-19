
n = int(input()
array = []
for _ in range(n):
    x = int(input())
    array.append(x)  


array = [0,10,0,10,1, 2, 3, 4, 5, 5, 5, 5, 6, 7, 8, 9, 1, 9]
sumValue = 10
list = []

for i in range(len(array)):
        j = i + 1
        for j  in range(len(array)):
            if (array[i] + array[j] == sumValue ):
                list.append(abs(array[i] - array[j]))
                

def unique_list(list):
    uniq_list = []
    uniq_set = set()
    for item in list:
       if item not in uniq_set:
            uniq_list.append(item)
            uniq_set.add(item)
    return uniq_list


print("Number of uniques pair = ", len(unique_list(list)))
