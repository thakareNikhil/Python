#The membership operator purpose is to check value in collection of another value
#it works on only iterable object means length of object is >1
# there are two type of operator in 'in' and 'not in'
# so 'in' operator is use for check value are their in object or not ,if their so it gives True if not their so it gives False
# so 'not in' operator is use for check value are not their in object ,if their so it gives False if not their so it gives True
a='HELLO'
b='122'
c=['a','b','c']
d={'1',1,'a','k'}
print('\t\tin:','h' in a )
print('\t\tin:','H' in a )
print('\t\tin:','1' in b )
print('\t\tin:','12' in b )
print('\t\tin:','a' in c )
print('\t\tin:',['a','b'] in c )
print('\t\tin:',1 in d )
print('\t\tnot in:','h' not in a )
print('\t\tnot in:','H' not in a )
print('\t\tnot in:','1' not in b )
print('\t\tnot in:','12' not in b )
print('\t\tnot in:','a' not in c )
print('\t\tnot in:',['a','b'] not in c )
print('\t\tnot in:',1 not in d )


