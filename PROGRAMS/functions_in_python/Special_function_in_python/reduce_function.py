"""3) reduce function: The purpose of reduce function is to get input iterable object element one by one and convert these elements in single value
or give the output in single values called int,float,complex,bool,str,list,set,tuple also by your requirement or input
reduce not present in default 'builtins' module ,for using reduce function we have required to import 'functools' module

syntax:1)functools.reduce(function ,iterable object) or 2)reduce(function,iterable object) you can use syntax 2 after 'from functools import reduce'

reduce function required to define two objects or variable in function
reduce function iterate the element from iterable abject and perform operation and store result in first variable
reduce function work on normal and portable function (lambda()) also

Some functions perform operation on iterable object but giving result in single value like sum(),''.join(),max(),min() it's
internally work on reduce function
 """
from functools import reduce#==> 'reduce' function present in 'functools' module and modules is set of functions
print('1]get the sum of list no with normal function')
def s(a,b):#function definition with two formal parameters because reduce function performing task on two object/variables
    return a+b #proces on inputs
a=list(map(int,input('entre no list:').split()))#getting input of list
b=reduce(s,a)#'s' is normal function call in reduce function , reduce passing inputs to these function and function perform tasks and return the
#result and reduce store these result in first variable (reduce internally works like that )
print('the sum of list is:',b,type(b))#reduce store the in result in first variable and define it's class name using elements store in iterable objects class name
#means you make list of str data so reduce make the object of <class:'str'> same like ,int,float,bool,complex also
print('='*50)

print('2] find the max and min no using lambda function')
a=list(map(int,input('entre no list:').split()))
b=reduce(lambda x,y: x if x>y else y,a)
c=reduce(lambda x,y: x if x<y else y,a)
print('the max no in list ',b,type(b))
print('the min no in list ',c,type(c))
print('='*50)

print('3]find the factorial of each no in list and make a list of these element and try to write these code in less lines')
#SEE the Beauty of the python
print(list(map(lambda x:reduce(lambda a,b:a*b,list(range(1,x+1))),list(map(int,input('entre list no :').split())))))
#here the combination of 'map' ,'lambda', and reduce function these code in one line  without defining any variable
print('='*50)

print('4]find the product of digits ')
a=int(input('entre no:'))
b=list(str(a))
c=reduce(lambda x,y:int(x)*int(y),b)#it's giving object of <class:'int'> because we give list iterable object and do type casting
print('the product of no, digits:',c,type(c))
print('='*50)

print('5]make a single list by getting collection nested /inner lists')
a=[[1,2,3],[4,5,6],[0,0,0],[9,4,6]]
print(reduce(lambda x,y:x+y,a))
print('='*50)

