#The purpose of Nested or inner while_loop is to execute the inner condition finite time until outer loop condition it becomes false
#The Nested while loop have two types 1] while_loop in for_loop 2]while_loop in while_loop
#until the outer it becomes false the inner loop perform operation repeatedly
print('while_loop IN while_loop')
print('1] Accept a no and print the multiplication table of each number within input no range')
a=int(input('Enter a no: '))
if a<=0:
    print('Please enter a positive integer')
else:
    print('MULTIPLICATION TABLE')
    i=1
    while i<=a:
        b=1
        while b<=10:
            print('{} x {} ={}'.format(i,b,b*i))
            b+=1
        else:
            print('The Multiplication Table of {}'.format(i))
        i+=1
    else:
        print('ALL MULTIPLICATION TABLES PRINTED')
print('END OF THE WHILE LOOP'.center(50,'='))
print('2] Accept a No. and print factorial of within input no range')
a=int(input('Entre Range: '))
if a<0:
    print('Please enter a positive integer')
else:
    print('FACTORIAL TABLE')
    i=0
    while i<=a:
        b=1
        c=1
        while c<=i:
            b=b*c
            c+=1
        else:
            print('The Factorial of {} is {}'.format(i,b))
        i+=1
    else:
        print('ALL FACTORIAL PRINTED')
print('END OF THE WHILE LOOP'.center(50,'='))
print('3]Accept a No.and Print all prime no within input no range')
a=int(input('Enter a range: '))
if a<2:
    print('Please enter a  no.>=2')
else:
    print('PRIME NO IN RANGE')
    i=2
    while i<=a:
        b=True
        c=2
        while c<i:
            if i%c==0:
                b=False
                break
            c+=1
        else:
            if b:
                print('{} is a prime number'.format(i))
        i+=1
    else:
        print('ALL PRIME NO IN RANGE')
print('END OF THE WHILE LOOP'.center(50,'='))
