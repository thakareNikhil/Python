#1)input get in function call
#2)process on input in function Body
#3)output/result in function Body
def string1(s):
    '''This use for print str'''
    print(f' Hello {s}! Welcome to function concept ')
a=input('Entre Your Name: ')
string1(a)
help(string1)


#1)input get in function Body
#2)process on input in function Body
#3)output/result in function Body
def string2():
    '''This use for print str'''
    a = input('Entre Your Name: ')
    print(f' Hello {a}! Welcome to function concept ')
string2()
help(string2)


#1)input get in function call
#2)process on input in function Body
#3)output/result in function call
def string3(s):
    '''This use for print str'''
    return s
a=input('Entre Your Name: ')
b=string3(a)
print(f' Hello {b}! Welcome to function concept ')
help(string3)


#1)input get in function Body
#2)process on input in function Body
#3)output/result in function call
def string4():
    '''This use for print str'''
    a = input('Entre Your Name: ')
    return a
b=string4()
print(f' Hello {b}! Welcome to function concept ')
help(string4)
