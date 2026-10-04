#Approach 1:
#2 Phases in function definition or Body part:
#1)input get in function Body
#2)process on input in function Body
#3)output/result in function call
print('1]Add Two No.')
def addon():#==>function header
    """This is tell about Function functioning """  #==> this is the str description of the function its optional
    a=int(input('Enter a number: '))#==>line 8 to 11 is function body or process function logic or indentation block
    b=int(input('Enter another number: '))#==>line 7 to 11 is function definition
    c=a+b#==> 'a','b','c' is local variables we can't call local variable in program part
    return a,b,c#==> return is flow transfer statement type its return the values
res=addon()#==>function call part ,'res' is the variable that store tuple values
print('sum: {} + {} is {} and types of res is {}'.format(res[0],res[1],res[2],type(res)))#==> we can call this tuple using indexing or slicing also
x,y,z=addon()
print('sum: {} + {} = {}'.format(x,y,z))#==>We can call this function variable using multiline variable definition also
a,b,c=addon()
print('sum: {} + {} = {} and type of function name is {}'.format(a,b,c,type(addon)))#==>We can use same name variables in program also but variables define in function call part
# are different and variables define in function definition part are different they no connection between because we can use variables and
# formal parameters define in function definition are allow to use in only function definition part we can not use in main body of the program
help(addon)#==> we can call function description using help(function name)
print('ALL TOPIC OF ABOVE IS USER DEFIN FUNCTION :Because user make function manually by their requirements and they call this function N of times in program for performing certain task/operation')
print('COMPLETE'.center(50,'='))


print('2]Area of Rectangle')
def AR():
    '''this is use for calculation of Area of Rectangle'''
    a=int(input('Enter a length: '))
    b=int(input('Enter a breadth: '))
    c=a*b
    return a,b,c
c=AR()
print('Area of Rectangle is {} x {} = {}'.format(c[0],c[1],c[2]))
help(c)
print('COMPLETE'.center(50,'='))


print('3]Area of Circle')
def AC():
    '''this is use for calculation of Area of Circle'''
    a=int(input('Enter a radius :'))
    b=3.14*a**2
    return a,b
A=AC()
print('Area of Circle is 3.14 x {} x {} = {}'.format(A[0],A[0],A[1]))
help(AC)
print('COMPLETE'.center(50,'='))