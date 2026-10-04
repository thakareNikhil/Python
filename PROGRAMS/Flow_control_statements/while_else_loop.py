"""#The purpose of while or while_else loop is to repeat the operation finite times if the condition is
not False after condition False the loop stop 'while' and 'else' is keywords
#The else part in while loop is optional
#The else part work in while loop after complete run indentation block then it goes in else part and run else block
#for define the while so initialization part,updation part is required if you don't define
it problems 'Name error' or run loop infinite times
#if you don't define test condition in while block so the PVM by default get as a False and execute else or other statements
#The initialization part means the loop start from condition"""

print('1]Which will generate 1 to n no')
a=int(input('Enter +ve no: '))
i=1#Initialization (start step)
if a<=0:
    print('Please enter a positive integer')
else:
    while i<=a:#while loop test condition is called as the end condition of loop
        print(i)
        i+=1#it's the updation part
    else:
        print('LOOP IS DONE')#it's the else part of loop it's run or execute after loop is complete or test condition is False
print(10*'=','COMPLETE',10*'=')
print('1]Which will generate n to 1 no')
a=int(input('Enter +ve no: '))
#i=1 =>In that case initialization is not required because it already defines as input
if a<=0:
    print('Please enter a positive integer')
else:
    while a>=1:
        print(a)
        a-=1
    else:
        print('LOOP IS DONE')
print(10*'=','COMPLETE',10*'=')
print('2]Which will generate even no to n')
a=int(input('Enter +ve no: '))
i=2
if a<=0:
    print('Please enter a positive integer')
elif a%2!=0:
    a=a-1
    while i<=a:
        print(i,'Even')
        i+=2
    else:
        print('LOOP IS DONE')
else:
    while i<=a:
        print(i,'Even')
        i+=2
    else:
        print('LOOP IS DONE')
print(10*'=','COMPLETE',10*'=')
print('3]Which will generate odd no to n')
a=int(input('Enter +ve no: '))
i=1
if a<=0:
    print('Please enter a positive integer')
elif a%2==0:
    a=a-1
    while i<=a:
        print(i,'Odd')
        i+=2
    else:
        print('LOOP IS DONE')
else:
    while i<=a:
        print(i ,'Odd')
        i+=2
    else:
        print('LOOP IS DONE')
print(10*'=','COMPLETE',10*'=')
print('4]Which will generate  in reverse even no n to 2')
a=int(input('Enter +ve no: '))
#i=2 not required because it's already input by user
if a<=1:
    print('Please enter a positive integer')
elif a%2!=0:
    a=a-1
    while a>=2:
        print(a,'Even')
        a-=2
    else:
        print('LOOP IS DONE')
else:
    while a>=2:
        print(a,'Even')
        a-=2
    else:
        print('LOOP IS DONE')
print(10*'=','COMPLETE',10*'=')
print('5]Which will generate in reverse odd no n to 1')
a=int(input('Enter +ve no: '))
if a<=0:
    print('Please enter a positive integer')
elif a%2==0:
    a=a-1
    while a>=1:
        print(a,'Odd')
        a-=2
    else:
        print('LOOP IS DONE')
else:
    while a>=1:
        print(a ,'Odd')
        a-=2
    else:
        print('LOOP IS DONE')
print(10*'=','COMPLETE',10*'=')
print('6]Which will generate the table of n')
a=int(input('Enter Table no you want to generate: '))
i=1
while i<=10:
    print(f'{a}x{i}={a*i}')
    i+=1
else:
    print('LOOP IS DONE')
print('Print str in char on line')
a=input()
i=0
while i<len(a):
    print(a[i])
    i+=1
else:
    print('LOOP IS DONE')