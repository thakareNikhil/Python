#The purpose of pass statement is to the bypass the conditions or loops
# if user define condition or loop, and later he wants to define indentation block so The 'pass' is use for that
#The 'pass' statement work is the bypass the condition or loop and execute else block
#The else block is required for defining 'pass' statement
#'pass' is the keyword
#the 'pass' statement is use as a 'continue' statement also
print('1]accept list from user and accept only positive no')
a=list(map(int,input('enter the list:').split()))
for i in a:
    if i<0:pass
    else:
        print(i,end=' ')