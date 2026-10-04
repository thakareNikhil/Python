a='Hello Python'
b=10
c=12.2
e=12.999299
d=range(11)
print(a)#print msg
print(b)#print 1 or more values
print('SUM OF {} and {} is {}'.format(b,c,b+c))#format function
print(f'{a}+{b}+{c}={b+c}')#same as format function
print('%d and %f and %s' %(b,c,a))#format specifiers %d=int,%f=float with by default 6 zeros,%s=str %e
print('%0.2e' %c)
print('%03.f and %d and %s' %(b,c,a))
print('round function {}'.format(round(e)))#round function increase value by using decimal is <=5
print('\t\t\t{}'.format(a))#/t use for tab space
print(' HELLO ITS CENTER FUNCTION '.center(40,'$'))#.center use for center the str values only
print(5*'=','Manually center',5*'=')
print(a,b,c,e,sep=' & ')#that use for separate the elements and add user defined str between
for i in d:
    print(i)
for k in d:#delegator use for horizontally print values "end=''"
    print(k,end=" ")
    print(k,end='=>')