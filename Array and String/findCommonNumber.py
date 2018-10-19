
a = [13,27,35,40,49,55,59]
b= [17,35,39,40,55,58,60]
hashMap =  {}

for num in a:
    hashMap[num] = 1
    
count = 0
for num in b:
    if(hashMap.get(num)):
        count += 1

print("count = ", count)
