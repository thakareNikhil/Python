#This is mostly recommended for performing operation if end-user input multiple values and multiple test condition
#The if_elif_else statements is recommended for performing operation if end-user input only one value and multiple test condition
#I can use this condition in both operation also but is get more space and time
#in this statement the else part is optional

print('print digit name')
a=int(input('Enter a Digit :'))
if a==0:
    print('ZERO')
elif a==1:
    print('ONE')
elif a==2:
    print('TWO')
elif a==3:
    print('THREE')
elif a==4:
    print('FOUR')
elif a==5:
    print('FIVE')
elif a==6:
    print('SIX')
elif a==7:
    print('SEVEN')
elif a==8:
    print('EIGHT')
elif a==9:
    print('NINE')
elif a>9:
    print('its +Ve no')
elif a<0 and a in range(-1,-10,-1):
    print('its -Ve digit')
else:
    print('its -Ve no')

