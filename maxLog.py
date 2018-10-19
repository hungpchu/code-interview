import operator
domain = "organisation1.com"
logs = ["user1@organisation1.com20180912", "user3@organisation2.com20180912", "user3@organisation1.com20180911", "user3@organisation1.com20180911" ]

domain1 = domain.split(".com")

d = "".join(domain1)

print(domain1)

result = []
hM = {}



# for c in logs:
#     c1 = c.split("@")
#     number = int(c1[1])
#     result.append(number)

# for num in result:
#     if(hM.get(num)):
#         hM[num] += 1
#     else:
#         hM[num] = 1
    
# print(max(hM.items(), key=operator.itemgetter(1))[0])
# print(result)


for c in logs:
    c = c.split(".")
    c1 = "".join(c)
    c1= c1.split("@")
    c2 = c1[1].split("com")
    # if (c1 == )
    if (c2[0] == d):
        result.append(c2[1])
    print(c2)
    
for num in result:
    if(hM.get(num)):
        hM[num] += 1
    else:
        hM[num] = 1
print (result)
print(hM)
print(max(hM.items(), key=operator.itemgetter(1))[0])
