
#This is mostly recommended for performing operation if end-user input multiple values and multiple test condition
#The if_else statements is not recommended for performing operation if end-user input only one value and multiple test condition
#I can use this condition in both operation also but is get more space and time


print('Identify the positive No.')
a=float(input('Enter a number :'))
if a<0:
    print(f'The {a} is -Ve')
else:
    if a>0:
        print(f'The {a} is +Ve')
    else:
        print(f'The {a} is 0')
print('COMPLETE'.center(50,'*'))
print('Identify the +Ve no is even or odd')
a=int(input('Enter a number :'))
if a%2==0 and a>0:
    print('The No {} is Even'.format(a))
else:
    if a%2!=0 and a>0:
        print('The No {} is Odd'.format(a))
    else:
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
else:
    if p<=0:
        print('The Amt is invalid:',p)
    if t<=0:
        print('The Time is invalid:',t)
    if r<=0:
        print('The Rate of Interest is:',r)
print('COMPLETE'.center(50,'*'))
print('Check String is palindrome or not')
a=input('Enter a STR :')
if a==a[::-1]:
    print('The Str obj is palindrome: ',a)
else:
    print('The Str obj is not palindrome: ',a)
print('COMPLETE'.center(50,'*'))
#that time if else statement is not recommended
print('print digit name')
a=int(input('Enter a Digit :'))
if a==0:
    print('ZERO')
else:
    if a==1:
        print('ONE')
    else:
        if a==2:
            print('TWO')
        else:
            if a==3:
                print('THREE')
            else:
                if a==4:
                    print('FOUR')
                else:
                    if a==5:
                        print('FIVE')
                    else:
                        if a==6:
                            print('SIX')
                        else:
                            if a==7:
                                print('SEVEN')
                            else:
                                if a==8:
                                    print('EIGHT')
                                else:
                                    if a==9:
                                        print('NINE')
                                    else:
                                        if a>9:
                                            print('its +Ve no')
                                        else:
                                            if a<0 and a in range(-1,-10,-1):
                                                print('its -Ve digit')
                                            else:
                                                print('its -Ve no')

