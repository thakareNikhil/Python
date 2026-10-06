"""1)global variables:Any variables define outside of is called global variable
There are two types of global variables:
a)user defined global variables:User defines global variables by their requirements outside the function
b)PVM defines by default global variables:PVM define global variables by default internally
The purpose of global variables is to minimize the local variables duplication in inside the function body part
means if user def two functions and make two local variables inside the functions with same value so program get extra memory
for same values for that type of situation we can define a single global variable outside the function but before function call
means you can define before function definition or after function definition also but, you can't define after function call because
after the function call global variables values not define but print inside the function and its give 'UnboundLocalError'
Because we print this variables names inside the function but function don't that variables values so that it gives 'UnboundLocalError'

There some operations we can perform on global variables:
1)For modifying the global variables inside the function:we have required define or call this global variables inside the
function using 'global' keyword it is mandatory ,without 'global' keyword we have required to make local variable ,define values of local
variables as values of global variable inside the function

2)For printing same values define in global variable means not update or modify so not required 'global' keyword its optional
"""
print('Without global variables')
def f():
    a='hello' #a,b is local variables
    b='Nikhil'
    print(a,b)
def g():
    c='hello' #c,d is local variables
    d='Mukesh'
    print(c,d)
#the point is there are 2 local variables in each function but 'a' & 'c' store same values means it is duplication and get more
#memory space
f()
g()
print('='*50)

print('With global variables after function definition')
def h():
    b='Nikhil'#b is local variables
    print(a,b,c)
def i():
    d='Mukesh' #d is local variables
    print(a,d,c)
a='Hello!' # a: is global variable
c=',what are you doing' # a: is global variable
h()#function call
i()#function call
print('='*50)

print('With global variables before function definition')
a='Hello!' # a: is global variable
c=',what are you doing' # a: is global variable
def h():
    b='Nikhil'#b is local variables
    print(a,b,c)
def i():
    d='Mukesh' #d is local variables
    print(a,d,c)
h()#function call
i()#function call
print('='*50)

print('modify global variables inside the function and store values in same variable name')
def j():
    global A
    A=A+10 #A is global variables
    print(A)
def k():
    global A
    A=A+20  #A is global variables
    print(A)
A=1 # a: is global variable
j()#function call
k()#function call
#we can not modify global variable inside the function without using 'global' keyword
#Every function call is update the value of global variables
#j() A=1 (ans:11) but in k() A=11 (ans:31) update the value in second function
print('='*50)

print('modify global variables inside the function and store values in different variable name')
def l():
    B=x+10 #x is global variables but define modified values in local variable B
    print(B)
def m():
    C=x+20 #x is global variables but define modified values in local variable C
    print(C)
x=1 # a: is global variable
l()#function call
m()#function call
#we can modify global variable inside the function without using 'global' keyword
#but the modified value define in different local variable or required to create local variable
#Every function call is not update the value of global variables because modified values store
# in local variable inside the function
#l() x=1 (ans:11) but in m() A=1 (ans:21)
print('='*50)

"""NameError"""
def X():
    a='Nikhil'
    print(r,a)
X()
r='Hello'
#we define global variable after the call so it's not consider function don't know 'r' value

"""UnboundLocalError"""
def X():
    r='Nikhil'+r
    print(r)
r='Hello'
X()
#we modify global variable  and store in same var_name so it's not consider
"""That Time We Use globals() :global function........."""