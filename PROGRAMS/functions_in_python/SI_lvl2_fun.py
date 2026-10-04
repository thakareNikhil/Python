#There are function go from three phases
#But in this level we divide and define three phases in three different functions
#ALL CONCEPT IN BELOW IS FUNCTION CHANNING or CHAIN
#Let's Start:
print('1]calculate SI using function definition call one function definition only?')
def Val():#function definition 1 for getting input only
    P=int(input('Enter Price: '))
    R=int(input('Enter Rate: '))
    T=int(input('Enter Time: '))
    return P,R,T
def C():#function definition 2 for processing on inputs
    a,b,c=Val()
    if a>0 and b>0 and c>0:
        SI=(a*b*c)/100
        TP=SI+a
        return SI,TP
    else:
        if a<=0:
            print('Invalid Price',a)
        if b<=0:
            print('Invalid Rate',b)
        if c<=0:
            print('Invalid Time',c)
        return "Can't calculate SI","can't calculate Total Price"
def P():#function definition 3 for giving result / output to user
    a,b=C()
    print('Simple Intrest is :',a)
    print('Total Price is :',b)

P()#function call
print('COMPLETE'.center(50,'='))


print('2]calculate SI using function definition call all functions definition?')
def val():#function definition 1 for getting input only
    P=int(input('Enter Price: '))
    R=int(input('Enter Rate: '))
    T=int(input('Enter Time: '))
    return P,R,T
def cal(a,b,c):#function definition 2 for processing on inputs
    if a>0 and b>0 and c>0:
        SI=(a*b*c)/100
        TP=SI+a
        return SI,TP
    else:
        if a<=0:
            print('Invalid Price',a)
        if b<=0:
            print('Invalid Rate',b)
        if c<=0:
            print('Invalid Time',c)
        return "Can't calculate SI","can't calculate Total Price"
def p(a,b):#function definition 3 for giving result / output to user
    print('Simple Intrest is :',a)
    print('Total Price is :',b)

a,b,c=val()#function call 1
x,y=cal(a,b,c)#function call 2
p(x,y)#function call 3
print('COMPLETE'.center(50,'='))
