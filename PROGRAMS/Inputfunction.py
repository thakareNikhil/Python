a=input('')#use getting input str
b=int(input(''))#use for getting input int
c=float(input(''))#use for getting float
d=input('Entre your name: ')#get input and also show title to user
print('Type a:{}'.format(type(a)))
print(f'Type b:'+str(type(b)))
print('Type c:%s'%(type(c)))
print('Type d:',type(d))
print('SUM: ',(int(input('Entre first no:'))+float(input('Entre second no:'))))#we can write code in a single line with input with output
print('SUM of is %0.3f'%((int(input('Entre first no:'))+float(input('Entre second no:')))))#we can use print functions are also
e=input('').split()#that input is mostly use for list input but str values only
print(e , type(e))
print(d.strip(' '))#that use for remove unuse spaces from start and end only enter by user