ip6 = "20dd:01:0db8:85a3:8A2E:0370:7334"

ip6 = ip6.split(':');
bol = True

for i in range(len(ip6)):
    if (ip6[i] == '' ):
        bol = False
        break

    if (len(ip6[i]) > 4):
        bol = False
        break
print bol 
