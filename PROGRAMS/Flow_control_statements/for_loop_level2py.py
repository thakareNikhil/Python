print('1]Calculate the sum of 1 to n natural no.')
a=int(input('Enter a number: '))
if a<0:
    print('entre valid no or +ve')
else:
    b=0 #addictive identity initialization
    for i in range(1,a+1):
        b=b+i
    else:
        print('sum of Natural no.:%d'%b)
print('COMPLETE'.center(40,'='))
print('2]Find square and cube of 1 to n no and do sum')
a=int(input('Enter a number: '))
if a<=0:
    print('entre valid no or +ve')
else:
    sqr=0#addictive identity
    cu=0#addictive identity
    for i in range(1,a+1):
        sqr=sqr+i**2
        cu=cu+i**3
        print('{}         {}         {}'.format(i,i**2,i**3))

    else:
        print('=' * 30)
        print('sum of sqr={} cube of={}'.format(sqr,cu))
print('COMPLETE'.center(40,'='))
print('3]Find the product or factorial of no and sun of factorial')
a=int(input('Enter a number: '))
if a<0:
    print('entre valid no or +ve')
else:
    b=1#multiplicative identity *
    c=0#addictive identity +
    for i in range(1,a+1):
        b=b*i
        c=b+c
        print('{} Factorial of No :{}'.format(i,b))
    else:
        print('=' * 30)
        print('factorial of no :{}'.format(b))
        print('Sum Of Factorial of no :{}'.format(c))
print('COMPLETE'.center(40,'='))
print('4]which will accept elements in list and sum of elements')
a=int(input('Enter a length of list:'))
if a<=0:
    print('entre valid length or +ve')
else:
    b=0#addictive identity
    c=[]
    for i in range(1,a+1):
       d=float(input(f'Enter a {i} element:'))
       b=b+d
       c.append(d)
    else:
        print('=' * 30)
        print('list :',c)
        print('Sum Of List element :',b)
        print('Average of List:',b/len(c))
print('COMPLETE'.center(40,'='))
print('5]Print the sum of digits in no')
a=int(input('Enter a number: '))
b=0#addictive identity
for i in str(abs(a)):
    b=b+int(i)
    print('Digits in No:', i)
else:
    print('=' * 30)
    print('sum of Digits in no:%0.2f'%b)
print('COMPLETE'.center(40,'='))
