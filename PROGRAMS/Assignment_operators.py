# The Assignment operator use for assign the one or more literal in variable one or multiple and swapping of variable values not using for str and  using for integer arithmetic operator
# There are only one assignment operator are here EQUAL TO :'='.
a=float(input('INT 1:'))
b=float(input('INT 2:'))
c=input('STR 1:')
d=input('STR 2:')
print(f'a={a}')# '=' that define the value in variable 'a'
print(f'b={b}')# '=' that define the value in variable 'b'
print(f'c={c}')# '=' that define the value in variable 'c'
print(f'd={d}')# '=' that define the value in variable 'd'
c,d=d,c # its means swaping the two variables values between them using '='
print('\t\t d in c:',c,'c in d:',d)# Interchanged the values between
a,b=c,d ## its means swaping the more variables values between them using '='
print(a,b,c,d)
a=10
b=3
a=a+b # swapping integer using arithmetic and assignment operator a=13
b=a-b #b=10
a=a-b #a=3
print('\t\t a:',a)
print('\t\t b:',b)
b=a*b # swapping integer using arithmetic and assignment operator b=30
a=b/a #a=10
b=b/a #b=3
print('\t\t a:',a)
print('\t\t b:',b)
x,y,z=10,20,30 # we are assign the more literals at a time in more variables using assignment operator
print('\t\t x:',x)#x=10
print('\t\t y:',y)#y=20
print('\t\t z:',z)#z=30
s,t,i=input(),int(input()),float(input())# we can get input also and '=' operator assign the value in variable by order define by end-user.
print('\t\t s:',s)#s=strobj
print('\t\t p:',t)#t=intobj
print('\t\t y:',i)#i=floatobj
print('='*50)

