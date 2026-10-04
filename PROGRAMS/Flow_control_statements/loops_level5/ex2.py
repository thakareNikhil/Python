print('1]Python program to find N largest elements from a list')
a=list(map(int,input('enter a list: ').split()))
b=int(input('enter a number: '))
a.sort(reverse=True)
print(a[:b])
print(a[-b:])
print('Complete'.center(20,'='))
print('2]Python program to print even and odd numbers in a list')
a=list(map(int,input('enter a list: ').split()))
for i in a:
    if i%2==0:
        print('EVEN',i)
    if i%2!=0:
        print('ODD',i)
print('Complete'.center(20,'='))
print('3]Python program to print all even and odd numbers in a range')
a=int(input('enter a number: '))
for i in range(1,a+1):
    if i%2==0:
        print('EVEN',i)
    if i%2!=0:
        print('ODD',i)
print('Complete'.center(20,'='))
print('4]Remove empty lsit from a list')
a=int(input('entr a list: '))
b=[]
d=[]
for i in range(a):
    c=input('enter a number: ').split()
    b.append(c)
for i in b:
    if len(i)>0:
        d.append(i)
print(d)
print('Complete'.center(20,'='))
print('5]Remove empty tuple from a list')
a=int(input('entr a list: '))
b=[]
d=[]
for i in range(a):
    c=tuple(input('enter a number: ').split())
    b.append(c)
for i in b:
    if len(i)>0:
        d.append(i)
print(d)
print('Complete'.center(20,'='))





