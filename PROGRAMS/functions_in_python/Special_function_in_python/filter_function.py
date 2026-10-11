"""1) filter :filter function use for filter the data from iterable object like list,str,tuple,set,dict using user defined conditions
define in function
syntax: filter(function name or function with condition , iterable object)

filter gives the output in memory address values means hexal decimal no.sytem form it's the object of <class:'filter'>
for make these memory address values to in understandable form we can convert using type casting methods and convert these object
values in list,set,tuple class
"""
print('1]Filter prime no from list using user defined function ')
def no(a):#function definition part
    b=True
    for i in range(2,a):#condition for checking prime no
        if a%i==0:
            b=False
    return b#return true if it not prime false if it prime
a=[int(i) for i in input('entre list of no:').split(',') if int(i)>=2]#input list no using list comprehension
d=filter(no,a)#filter function 'no' is function call to user defined function, 'a' is iterable object or list of no
#filter iterate element from 'a' list and send in 'no' condition these function checks these values is prime or not and give
#boolean values if 'no' returns true its accept these element if 'no' return false it escape these, element that is called filtration process
#we do using filter function it make other iterable object with filter values we can access these elements through type casting
print('Filter object :',d,type(d))
c=list(d)#these process is type casting that convert <class:'filter'> object into <class:'list'> object
print('list object :',c,type(c))
print("="*50)

print('2]filter even no using lambda function')
a=[int(i) for i in input('entre list of no:').split(',')]
b=list(filter(lambda x:x%2==0,a))
print(b,type(b))
print('='*50)

print('3]filter vowel contain word in one line code')
print('Vowels list',list(filter(lambda x:not set(x).isdisjoint(set('aeiou')),input('entre string:').split())))
print('Consonant list',list(filter(lambda x:set(x).isdisjoint(set('aeiou')),input('entre string:').split())))
print('='*50)

print('4]filter the no that divisible by 7')
print('No. that divisible by 7',list(filter(lambda x:x%7==0,[int(i) for i in input('entre no list : ').split()])))
#see the python beauty that make code so portable using special functions or anonymous functions
print('='*50)

print('5] filter the words these length is prime no')
def check(a):
    b=True
    for i in range(2,len(a)):
        if len(a)%i==0:
            b=False
    return b

a=[i for i in input('entre str:').split() if len(i)>=2]
b=list(filter(check,a))
print('list words these length is prime no',b)
#at that place we can't use lambda function because lambda is giving instant result in possible cases not all
#but that place we have required perform some operation on elements
print('='*50)