print('1]Check voter is eligible for vote or not if th condition is not true ask to user entre your age repeatable')
while True:
    a=int(input('Entre Your age:'))
    if a>=18 and a<=100:
        print('You are eligible for vote')
        break
    else:
        print('You are not eligible for vote')
print('END OF PROGRAM'.center(50,'='))


print('2]Find max and Min no. from list without using any function only use for getting list input ')
a=int(input('entre range of list : '))
c=[]
if a<=0:
    print('Invalid range')
else:
    for i in range(a):
        b=int(input(f'entr element {i+1} :'))
        c.append(b)
    d=c[0]
    for i in c[1:]:
        if i>d:
            d=i
    else:
        print('The MAX VALUE IN LIST :',d)
print('END OF PROGRAM'.center(50,'='))
