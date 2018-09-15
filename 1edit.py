string = "pale"
edit = "lep"
count = 0
count1 = 0
bol = True

for i in range(len(string)):
    for j in range(len(edit)):
        if (string[i] != edit[j] and i == j):
            #print edit[j]
            #bol = False
            count += 1
        elif ( string[i] == edit[j] ):
            count1 += 1
            print edit[j]
if (len(string) - count1 == 1):
    count = 1
if ( count > 1):
    bol = False

if(len(edit) - len(string) == 1):
    bol = True
elif ( len(edit) - len(string) > 1):
    bol = False


print bol
