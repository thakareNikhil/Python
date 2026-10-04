print('while_loop in for_loop')
print('1] Accept a no and print the multiplication table of each number within input no range')
a=int(input('Enter a Range : '))
if a<=0:
    print('ENTRE +VE RANGE')
else:
    print('MULTIPLICATION TABLES')
    for i in range(1,a+1):
        b=1
        while b<=10:
            print('{} x {} ={}'.format(i,b,i*b))
            b+=1
        else:
            print('THE MULTIPLICATION TABLE OF %d'%i)
    else:
        print('TABLE PRINTING COMPLETE')
print('END OF PROGRAM')
print('2] Accept a No. and print factorial of within input no range')
a=int(input('Enter a Range : '))
if a<0:
    print('please enter a positive integer')
else:
    print('FACTORIAL TABLE')
    for i in range(a+1):
        b=1
        c=1
        while b<=i:
            c=c*b
            b+=1
        else:
            print('The Factorial of {} is {}'.format(i,c))
    else:
        print('THE FACTORIAL TABLE IS COMPLETE')
print('END OF PROGRAM')
print('3]Accept a No.and Print all prime no within input no range')
a=int(input('Enter a Range : '))
if a<2:
    print('ENTRE NO >=2')
else:
    print('PRIME NO')
    for i in range(2,a+1):
        b=2
        c='PRIME'
        while b<i:
            if i%b==0:
                c='NOT PRIME'
            b+=1
        else:
            print('{} is {} No'.format(i,c))
    else:
        print('PRIME NO PRINTING COMPLETE')
print('END OF PROGRAM')