def mean(two_d_array):
    # Write your code here
       # Write your code here
    result = []
    num = 0
    result1 = 0
    count = 0
    if (len(two_d_array) < 1 or len(two_d_array) > 10 ):
            return
    for r in two_d_array:
        if (len(r) < 1 or len(r) > 10):
            return
        for c in r:
            if ( c < -25000 or c > 25000):
                return
            num += c
            count += 1
            if (count == len(r)  ):
                result1 = num/len(r)
                if (isinstance(result1, float)):
                    print("result1 = ",result1)
                    result1 = "{0:.1f}".format(result1)
                result.append(result1)
                num = 0.0
                count = 0
    return result
    # return [ "{0:.1f}".format(sum(row)/len(row)) for row in two_d_array]
    
array = [{1,2},{1,2}]

print(mean(array))
