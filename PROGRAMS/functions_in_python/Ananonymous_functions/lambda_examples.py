print('1]check even or odd no')
Check=lambda a:'Even' if a%2==0 else 'Odd'
x=int(input('entre no:'))
print(Check(x))

print('2]check str is palindrome or not')
print((lambda x:'palindrome' if x==x[::-1] else 'Not palindrome')(input('Entre string:')))

print('3]check no. is prime or not')
def prime(n):
    a=True
    for i in range(2,n):
        if n%i==0:
            a=False
            break
        return a
n=int(input('entre no:'))
check=lambda x:'invalid'if x<=1 else 'Prime' if prime(x) else 'Not prime'
print(check(n))

print('4]Calculate Simple interest ')#See the beauty of python how lambda make code portable
print((lambda x,y,z:f'the simple interest is:{(x*y*z)/100}')(int(input('entre price:')),int(input('entre Time:')),int(input('entre Rate:'))))

print('5]find max no. without using max()')
def MAX(a):
    b=a[0]
    for i in a[1:]:
        if i>b:
            b=i
    return b

x=a=list(map(int,input('entre list:').split()))
check=lambda a:f'The Max no is {MAX(a)}'
print(check(x))

print('6]find min no. without using min()')
def MIN(a):
    b=a[0]
    for i in a[1:]:
        if i<b:
            b=i
    return b

x=a=list(map(int,input('entre list:').split()))
check=lambda a:f'The Min no is {MIN(a)}'
print(check(x))

print('7]sort list using 2 element using lambda')
a=[('nk',99),('mp',80),('vt',45),('pm',500)]
a.sort(key=lambda x:x[1])
print(a)