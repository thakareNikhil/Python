"""2)map() function:The purpose of map function is iterate the values from iterable object or modify that values or perform
operation on each element or value and store object of <class:'map'> in encrypted no systems like hexal its giving memory address
so we can be performing type casting method and convert these whole memory address in list,tuple,set object class

syntax:map(function call/portable function/class name,iterable object) make the object of <class:'map'>
map is the function that work on using user defined function condition or classes iterate element one by one and perform operation
each element by the condition and make another object sore these modified values

we can use functions or class also use inside these functions because in python, language class or functions are both are callable
we can prove using 'callable()' print(callable(int)) ==>True ==>'int' is a class
                                print(callable(map)) ==> True ==>'map' is a function
                                but both result come same ,it's prove

"""
print('1]accept no list and convert these no in its square using lambda function ')
a=[int(i) for i in input('entre list of no:').split()]
b=map(lambda x:x**2,a)#perform operation on each element using map()
print(b,type(b))
c=list(b)#perform type casting make <class:'map'> object into <class:'list'> object
print('These is list of square of above list:',c,type(c))
print('='*50)

print('2]accept no list and convert these no in its factorial no using user defined function')
def f(a):
    b=[]
    for i in range(1,a+1):
        b.append(i)
    c=1
    for i in b:
        c=c*i
    return c
a=[int(i) for i in input('entre list of no:').split() if int(i)>=0]
b=list(map(f,a))
print('Factorial list:',b)
print('='*50)

print('3] make list of length of each word')
print('list of length of word:',list(map(lambda x:len(x),input('entre str:').split())))
#see the python beauty make code so portable
print('='*50)

print('4]get list input using class')
a=list(map(int,input('entre list of no:').split()))
b=list(map(float,input('entre list of no:').split()))
c=list(map(bool,input('entre list of no:').split()))
d=list(map(str,input('entre list of no:').split()))
e=list(map(str.upper,input('entre list of no:').split()))
f=list(map(str.title,input('entre list of no:').split()))
#we can call classes functions also inside the map() but without parenthesis '()'
print(a)
print(b)
print(c)
print(d)
print(e)
print(f)
#int,float,bool are called class but in python class or function both are callable
print('='*50)


print('how to combine 2 or more  list and make single list ')
#using map()
print(list(map(lambda x:(x,x**2),[1,2,3,4,5,6,7,8,9,])))
#using zip
a=[1,2,3,4,5,6,7,8,9]
b=list(map(lambda x:x**3,a))
c={}
for k,v in zip(a,b):#we can make dict also
    c[k]=v
print(c)

for i in zip(a,b):#we print single object list also
    print(list(i))

a=input('entre str :').split()
print(list(map(lambda x:{x:len(x)},a)))



