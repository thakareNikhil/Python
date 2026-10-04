#The purpose of for loop is to repeat the operation using the length of iterable objects times only
#The for loop is run length of iterable object times and after complete then run the other statements in program
#In for loop have not required initialization ,condition ,and updation part but it required define variable in for loop
#The for loop run or execute only iterable object by using their length it not execute uniterable objects it shows error
#the iterable datatypes it will accept str,bytes,bytearray,range,set,list,tuple,frozenset,dict
#it will be not accepted int,float,bool,complex,None type, it trows error
#it can't run infinite times like while loop
#'for' ,'in' there are keywords use in for loop
#The for loop contain else part also the 'for_else' loop if user define and else part is optional
#after complete the execution of for (block of statement) loop the else part block of statement is execute
#after defining for loop the indentation is mandatory without indentation is not run the indentation block
print('hello world 3 times')
for i in range(3):
    print('Hello world')
print('Done='*10)
print('1 to n no. and n to 1')
a=int(input('enter a number'))
for i in range(1,a+1):
    print(i)
for i in range(a,0,-1):
    print(i)
else:
    print('done'.center(20,'='))
print('Print Mul Table')
a=int(input('enter a number'))
for i in range(a,a*10+a,a):
    print(i,end=' ')
for i in range(a*10,a-1,-a):
    print(i,end=' ')
else:
    print('done'.center(20,'='))
print('print even no 2 to n and odd no 1 to n')
a=int(input('enter a number'))
for i in range(2,a+1,2):
    print('even',i)
for i in range(1,a+1,2):
    print('odd',i)
else:
    print('done'.center(20,'='))
