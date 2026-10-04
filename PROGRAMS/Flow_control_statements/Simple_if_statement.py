#The simple if statements is mostly recommended for performing operation if end-user input only one value and multiple test condition
#This is not recommended for performing operation if end-user input multiple values and one test condition
#I can use this condition in both operation also but is get more space and time

print('Identify the positive No.')
a=float(input('Enter a number :'))
if a<0:
    print(f'The {a} is -Ve')
if a>0:
    print(f'The {a} is +Ve')
if a==0:
    print(f'The {a} is 0')
print('COMPLETE'.center(50,'*'))
print('Identify the +Ve no is even or odd')
a=int(input('Enter a number :'))
if a%2==0 and a>0:
    print('The No {} is Even'.format(a))
if a%2!=0 and a>0:
    print('The No {} is Odd'.format(a))
if a<=0:
    print('The No is {} -Ve or Zero'.format(a))
print('COMPLETE'.center(50,'*'))
print('Calculate the simple interest')
p=int(input('Enter a Amt :'))
t=int(input('Enter a Time :'))
r=int(input('Enter a Rate of Interest :'))
#The end-user input three times so that time simple if statement is not recommended
if p>0 and t>0 and r>0:
    print('\t\t\tThe input is Valid')
    print('The simple interest is:{} '.format((p*t*r)/100))
if p<=0:
    print('The Amt is invalid:',p)
if t<=0:
    print('The Time is invalid:',t)
if r<=0:
    print('The Rate of Interest is:',r)
print('COMPLETE'.center(50,'*'))
print('Check String is palindrome or not')
a=input('Enter a STR :')
#The end-user input one time so that time simple if statement is recommended
if a==a[::-1]:
    print('The Str obj is palindrome: ',a)
if a!=a[::-1]:
    print('The Str obj is not palindrome: ',a)
print('COMPLETE'.center(50,'*'))
print('print digit name')
a=int(input('Enter a Digit :'))
if a==0:
    print('ZERO')
if a==1:
    print('ONE')
if a==2:
    print('TWO')
if a==3:
    print('THREE')
if a==4:
    print('FOUR')
if a==5:
    print('FIVE')
if a==6:
    print('SIX')
if a==7:
    print('SEVEN')
if a==8:
    print('EIGHT')
if a==9:
    print('NINE')
if a>9:
    print('its +Ve no')
if a<0 and a in range(-1,-10,-1):
    print('its -Ve digit')
else:
    print('its -Ve no')

