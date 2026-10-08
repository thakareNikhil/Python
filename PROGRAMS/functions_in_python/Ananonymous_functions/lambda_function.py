"""Anonymous Lambda function:The purpose of these function is to perform instance operation
This function is use for perform on solving small task and get instant result.
'lambda' is a keyword use in to defining anonymous function that is called lambda function
we can perform small operation like normal function in lambda function also for getting instant result ,the lambda function
is portable function we can use inside the object or inside the functions also for getting specific result
ex:we can use on that list,set,tuple etc. datatypes for performing instant operation using other function map,reduce,filter etc.

syntax: varname=lambda list of formal parameters/positional arguments:expression

varname=it's a variable name or lambda function name object of <class:'function'>
lambda=it's a keyword to define lambda or anonymous function
list of formal parameters/positional arguments= this is the parameters list that holds the input
expression=we can process of those inputs mean perform required operation like sum,max(),mul,div etc .
we can define the lambda function in single line without using 'return' statement or keyword

lambda function is precise(short) the code as compare to normal function
"""
print('without using lambda function (normal function)')
def Sum(a,b):
    return a+b
a=int(input('entre no :'))
b=int(input('entre no :'))
print(Sum(a,b))
print('='*50)

print('with using lambda function')
a=int(input('entre no :'))
b=int(input('entre no :'))
print((lambda x,y:x+y)(a,b))#syntax 1

print((lambda x,y:x+y)(int(input('entre no :')),int(input('entre no :'))))#syntax 2 : lambda became portable perform all this in one line

add=lambda a,b:a+b #syntax 3:perform operation and define like normal function also
result=add(a,b)
print(result)
#we can use lambda function inside the functions also like map(lambda()),filter(lambda()),reduce(lambda())
print('='*50)


