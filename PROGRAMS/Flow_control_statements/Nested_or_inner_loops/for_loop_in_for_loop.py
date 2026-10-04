#The purpose of Nested or inner for_loop is to execute the inner condition finite time until outer loop condition it becomes false
#The Nested for loop have two types 1] for_loop in for_loop 2]for_loop in while_loop
#until the outer it becomes false the inner loop perform operation repeatedly
print('THIS IS for_loop IN for_loop')
print('1]accept a no. and print the multiplication table of each number within input no range')
a=int(input('Enter a range : '))
if a<=0:
    print('Please enter a positive integer')
else:
    print('MULTIPLICATION TABLES')
    for i in range(1,a+1):
        print('Multiplication Table of {}'.format(i))
        for k in range(1,11):
            print('{} x {} ={}'.format(i,k,i*k))
        else:
            print('The multiplication table of {} is completed'.format(i))
    else:
        print('ALL TABLE ARE PRINTED WHITHIN NUMBER')
print('END OF PROGRAM'.center(50,'='))
print('2] Accept a No. and print factorial of within input no range ')
a=int(input('Enter a range : '))
if a<0:
    print('Please enter a positive integer')
else:
    print('FACTORIALS')
    for i in range(0,a+1):
        b=1#multiplicative identity
        for k in range(1,i+1):
            b=b*k
        else:
            print('The Factorial of {} is {}'.format(i,b))
    else:
        print('ALL FACTORIAL ARE PRINTED WHITHIN NUMBER')
print('END OF PROGRAM'.center(50,'='))
print('3] Accept a No.and Print all prime no within input no range')
a=int(input('Enter a range : '))
if a<=1:
    print('please enter range greater than >=2')
else:
    for i in range(2,a+1):
        b=True
        for j in range(2,i):
            if i%j==0:
                b=False
                break
        else:
            if b:
                print(i,'is Prime No')
    else:
        print('ALL PRIME NUMBER ARE PRINTED WHITHIN NUMBER %d'%a)
print('END OF PROGRAM'.center(50,'='))