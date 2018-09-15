a = 'bacdef'
b = 'agggcbdef'

c = ''.join(sorted(a))
d = ''.join(sorted(b))

if ( c == d ):
    print c
    print d
    print 'true'
else:
    print 'false'
