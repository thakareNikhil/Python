"""globals(): we use this function at if we modify value in inside the function and store in same variable name or access all
global variables user defined and PVM default define internally also
globals() is a function that created inside the function definition body and, it makes object of <class:'dict'> and store the
all global variable with their keys and values
We can print all global variables outside of the function at a time with var_name and var_values or seperate also
After define globals() and storing keys and values in object of <class:'dict'> we can perform or use dict dataype functions or operationes on that
"""
print('global() function object of <class:"dict">')
def Global():
    a=globals()#==>globals() function store all global variables in object of dict class
    print('='*50)
    print(a)
    print('=' * 50)
    print(type(a))
    print('=' * 50)
    print(len(a))
b=10
c=20
Global()
#We can modify,update and access keys and values using dict functiones
#get(),update(),copy(),clear(),keys(),values(),items(),pop(),popitems()
print('='*50)
def access():
    Dict=globals()
    print('a =',globals().get('a'),'b =',globals().get('b'))
    print('a =',Dict['a'], 'b =',Dict['b'])
    print('a =', globals()['a'], 'b =', globals()['b'])
    for k,v in Dict.items():
        print('keys',k,'& Values',v)
#There are the ways of printing global variables values
a=10
b=20
access()
#globals() is a dict object that store global variables names as keys of dict and values as values of dict
