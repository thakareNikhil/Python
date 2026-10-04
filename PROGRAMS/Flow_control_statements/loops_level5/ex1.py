print('WELCOME TO LOOPS LEVEL 5')
print('1]Python program to interchange first and last elements in a list')
a=int(input('Entre range :'))
b=[]
if a<=0:
    print('entre valid range')
else:
    for i in range(a):
        c=input(f'entre element {i+1} :')
        b.append(c)
print(b)
b[0],b[-1]=b[-1],b[0]
print(b)
print('Complete'.center(50,'='))
print('2]Python program to swap two elements in a list')
a=input('entre list :').split()
print(a)
a[0],a[-1]=a[-1],a[0]
print(a)
print('Complete'.center(50,'='))
print('''3]Python | Ways to find length of list
Python | Ways to check if element exists in list''')
a=input('entre list :').split()
if len(a)==0:
    print('list empty')
else:
    print(len(a))
print('Complete'.center(50,'='))
print('4]Different ways to clear a list in Python')
a=input('entre list :').split()
for i in a:
    a.remove(i)
else:
    print(a,len(a))
print('Complete'.center(50,'='))
print('5]Python | Reversing a List')
a=input('entre list :').split()
b=[]
for i in a[::-1]:
    b.append(i)
else:
    print(b)
print('Complete'.center(50,'='))
print('6]Python program to find sum of elements in list')
a=input('entre list :').split()
b=0
for i in a:
    b=b+int(i)
else:
    print('SUM:',b)
print('Complete'.center(50,'='))
print('7]Python | Multiply all numbers in the list')
a=input('entre list :').split()
b=1
for i in a:
    b=b*int(i)
else:
    print('MULTIPLICATION:',b)
print('Complete'.center(50,'='))
print('8]Python program to find smallest number in a list')
a=input('entre list :').split()
b=int(a[0])
for i in a[1:]:
    if int(i)<b:
        b=int(i)
else:
    print('MIN :',b)
for i in a[1:]:
    if int(i)>b:
        b=int(i)
else:
    print('MAX :',b)
print('9]Python program to find second largest number in a list')
a=input('entre list :').split()
b=int(a[0])
for i in a[1:]:
    if int(i)>b:
        b=int(i)
else:
    a.remove(str(b))
    b=int(a[0])
    for i in a:
        if int(i)>b:
            b=int(i)
    else:
        print('SECOND LARGE NUMBER :',b)