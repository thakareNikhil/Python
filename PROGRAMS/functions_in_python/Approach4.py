#Approach 3:
#All Phases in function Body part:
#1)input get in function Body
#2)process on input in function Body
#3)output/result in function Body
print('1]Add Two No.')
def addon():#==>function header 'a' and 'b' is the list of formal parameters we can't use in program part without define
    """This is tell about Function functioning """  #==> this is the str description of the function its optional
    a = int(input('Enter a number: '))
    b = int(input('Enter another number: '))
    c=a+b#==> 'c' is local variable we can't use in program part without define
    print('SUM : {} + {} = {}'.format(a, b, c))#==>Output in function Body part
addon()#==>function call
help(addon)#==> we can call function description using help(function name)
print('ALL TOPIC OF ABOVE IS USER DEFIN FUNCTION :Because user make function manually by their requirements and they call this function N of times in program for performing certain task/operation')
print('COMPLETE'.center(50,'='))


print('2]Area of Rectangle')
def AR():
    '''this is use for calculation of Area of Rectangle'''
    x=int(input('Enter a length: '))
    y = int(input('Enter a breadth: '))
    z=x*y
    print('Area of Rectangle is {} x {} = {}'.format(x, y, z))
AR()
help(AR)
print('COMPLETE'.center(50,'='))


print('3]Area of Circle')
def AC():
    '''this is use for calculation of Area of Circle'''
    r = int(input('Enter a radius :'))
    A=3.14*r**2
    print('Area of Circle is 3.14 x {} x {} = {}'.format(r, r, A))
AC()
help(AC)
print('COMPLETE'.center(50,'='))