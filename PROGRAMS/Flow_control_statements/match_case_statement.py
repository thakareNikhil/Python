#The match case statement is purpose is performing operation on Menu driven application or choice
#The 'match' and 'case' keywords in soft kwlist
#The match case statement work on predefined condition in case keyword
#match is input the choice from user and execute the case using choice and match allows only , int,str and bool type of input only
#user choice is match with case condition so only that case block of code is run and run other statement if you define
#if user match with case 1 so it run the block of code in case 1 and other statement
#if user match with case 2 so it run the block of code in case 2 and other statement
#if user input is not match with cases the math case statement default case is called case _: so that case is run by default
#the case _: this case is not mandatory to right and is allow to right at the last of the all cases
#There are two type of exit 1]logical exit (break) =that is use only loops ,1]physical exit (exit()): that exit is allows in match case
#'break' is break the loop and execute other statement but 'exit()' is exit from case but not execute the other statement
#if user want to define two conditions in case statement so its define using bitwise or'|' and bitwise and'&' operator only
#The match giving only one output and execute only one case at a time , the match case is imported in python version 3.10.00 before is not there
print('''		Areas of Different Figures
					===================================================
							C . Circle
							R. Rectangle
							S: Square
							T. Triangle
							E. Exit		''')
a=input('enter your choice: ')
match a:
    case 'C'|'c':
        r=int(input('Enter Radius:'))
        if r>0:
            print('Area of Circle :',3.14*r**2)
        else:
            print('invalid Radius')

    case 'R'|'r':
        l=int(input('Enter Length:'))
        b=int(input('Enter Breadth:'))
        if l>0 and b>0:
            print('Area of Rect :',l*b)
        else:
            if l<=0:
                print('invalid Length')
            if b<=0:
                print('invalid Breadth')
    case 'S'|'s':
        s=int(input('Enter Side:'))
        if s > 0:
            print('Area of Square :',s*s)
        else:
            print('invalid Side')

    case 'T'|'t':
        b=int(input('Enter Base:'))
        h=int(input('Enter Height:'))
        if h > 0 and b > 0:
            print('Area of Triangle :',(1/2)*h*b)
        else:
            if b <=0:
                print('invalid Base')
            if h <=0:
                print('invalid Height')
    case 'E'|'e':
        exit()
    case _:
        print('Invalid option')
print("COMPLETE"*10)
print('''================================
       ABC BANK
================================'''.center(10,' '))
a=''
b=''
while a!=12345:
    a=int(input('Enter Account Number: '))
else:
    print('Your account number is Found ')
while b!=409409:
    b=int(input('Enter PIN: '))
else:
    print(f'''
Account Number: {a}
PIN: {'*'*len(str(b))}

Login Successful!

1. Check Balance
2. Deposit
3. Withdraw
4. Change PIN
5. Exit''')
A=int(input('Entre no for choose option :'))
B=float(1098726)
match A:
    case 1:
        print(f' Available Balance :{B}INR')
        exit()
    case 2:
         x=float(input('Entre Deposit AMT :'))
         y=int(input('PIN :'))
         if y==b:
             B=x+B
             print('Deposit Successful!',B)
         else:
             print('input correct PIN:')
         exit()
    case 3:
        x=int(input('Entre Withdraw AMT :'))
        y=int(input('PIN :'))
        if y==b:
            B=B-x
            print('Withdraw Successful!',B)
        else:
            print('input correct PIN:')
        exit()
    case 4:
        x=int(input('Entre New PIN:'))
        y=int(input('PIN :'))
        if y==b:
            print('Your PIN Change Successful!',x)
            x = b
        else:
            print('input correct PIN:')
        exit()
    case 5:
        exit()
    case _:
        print('Invalid option')

