ip = '0000.11.22.257'
ip = ip.split('.')
#print(int("0001h"))
bol = True
count = 0

print ("ip = ", ip)
def number(string):
    try:
        int(string)
        return True
    except ValueError:
        return False
    
for i in range(len(ip)): 
    if(number(ip[i]) != True ):

        print("len ip[i] =", len(ip[i]))
        bol = False
        if (count == 4):
            count = 0
        count += 1

    if ( len(ip[i]) <= 0 or len(ip[i]) > 4):
        bol = False
    if ( bol == True ):
        if (int(ip[i]) < 0 or int(ip[i]) > 255):
            print "hung"
            bol = False


    

       
        
        
        
        
      
    
  
      

        
 
    #print type(c)

print bol
print(8 % 4)
