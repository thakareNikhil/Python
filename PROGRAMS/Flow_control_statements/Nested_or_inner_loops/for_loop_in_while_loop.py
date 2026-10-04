print('THIS IS for_loop IN while_loop')
print('1] Accept a no and print the multiplication table of each number within input no range')
a=int(input('Enter a range : '))
if a<=0:
    print('Please enter a positive integer')
else:
    print('MULTIPLICATION TABLES')
    i=1
    while i<=a:
        for j in range(1,11):
            print('{} x {} ={}'.format(i,j,i*j))
        else:
            print('Print The Multiplication Table of {}'.format(i))
        i+=1
    else:
        print('ALL TABLE ARE PRINTED WHITHIN NUMBER')
print('END OF PROGRAM'.center(50,'='))
print('2] Accept a No. and print factorial of within input no range')
a=int(input('Enter a range : '))
if a<=0:
    print('please enter a positive integer')
else:
    print('FACTORIALS')
    i=1
    while i<=a:
        b=1
        for j in range(1,i+1):
            b=b*j
        else:
            print('The Factorial {} is {}'.format(j,b))
        i+=1
    else:
        print('ALL FACTORIAL ARE PRINTED WHITHIN NUMBER')
print('END OF PROGRAM'.center(50,'='))
print('3]Accept a No.and Print all prime no within input no range')
a=int(input('Enter a range : '))
if a<=0:
    print('please enter a positive integer')
else:
    i=2
    while i<=a:
        b=True
        for j in range(2,i):
            if i%j==0:
                b=False
        else:
            if b:
                print('{} IS PRIME NO'.format(i))
        i+=1
    else:
        print('ALL PRIME NO ARE PRINTED WHITHIN NUMBER')

