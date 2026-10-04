print('1]generate the multiplication table of input and call only 1 function in program ?')
def I():#function definition 1
    a=int(input('Entre No.:'))
    if a<=0:
        return 'Invalid Input'
    else:
        return a
def M():#functon definition 2
    m=I()
    for i in range(1,11):
        print(f'{m} x {i} = {m*i}')
    else:
        return f'Table Of {m}'
M()#function call
print('COMPLETE'.center(50,'='))


print('2]generate the multiplication table of input and call all function in program ?')
def In():#function definition 1
    a=int(input('Entre No.:'))
    if a<=0:
        return 'Invalid Input'
    else:
        return a
def Mul(m):#function definition 2
    for i in range(1,11):
        print(f'{m} x {i} = {m*i}')
    else:
        return f'Table Of {m}'
a=In()#function call 1
Mul(a)#function call 2
print('COMPLETE'.center(50,'='))