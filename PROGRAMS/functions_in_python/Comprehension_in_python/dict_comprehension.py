"""3)dict comprehension:We can perform use for loop and for loop with conditional statement if only not else inside dict object notationes {}
its is use for short or precise the code but, we have required define two variables in for loop becaouse dict store keys and values
"""
print('1] separate that student name and his age>=18' )
a={'nt':12,'kt':13,'fg':22,'vt':40,'sky':24,'mg':68}
b={k:v for k,v in a.items() if v>=18}
print(a)
print(b,type(b))
print('Complete'.center(50,'='))

print('2]invert keys and values and make dict keys==values and values==keys')
b={v:k for k,v in a.items()}
print(b,type(b))
print('Complete'.center(50,'='))

print('accept a string and divide in digits:val,alphabets:val,special symbal:val')
a={'digits':[],'alphabets':[],'special symbal':[]}
b=input('Entre A string :').split()
a['digits']=[i for i in b if i.isdigit()]
a['alphabets']=[i for i in b if i.isalpha()]
a['special symbal']=[i for i in b if not i.isdigit() or not i.isalpha()]
print(a)