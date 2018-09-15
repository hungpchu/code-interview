listVideo = [('abc',10),('def',15),('ghi',10),('abc',12),('xyz',100)]

print(sorted(listVideo, key=lambda topRate: topRate[0], reverse=True))



def getName(lst):
    names = set()
    for x in lst:
        names.add(x[0])
    return list(names)

print(getName([('abc',10),('def',15),('ghi',10),('abc',12),('xyz',100)]))
