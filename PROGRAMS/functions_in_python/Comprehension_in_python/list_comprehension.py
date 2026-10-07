"""1)list comprehension:We can perform use for loop and for loop with conditional statement if only not else inside list object notationes []
its is use for short or precise the code
"""
print('without list comprehension ')
print('1]separate the even no. from list')
a=[1,2,3,4,5,6,7,7,8,8,9,0,22,88]
b=[]
for i in a:
    if i%2==0:
        b.append(i)
print(b)
print('COMPLETE'.center(50,'='))

print('with list comprehension')
print(list(i for i in a if i%2==0)) #compress the code and make in single line syntax(1)
print([i for i in a if i%2==0]) #compress the code and make in single line syntax(2)
b=[i for i in a if i%2==0]
print(b,type(b)) #compress the code and make in two lines syntax(3)
print([i for i in input().split() if int(i)%2==0])#==>syntax 4
print('COMPLETE'.center(50,'='))

print('2]Accept string and separate the vowels contain word')
a=input('Enter a string :').lower().split()
b=set('aeiou')
c=[i for i in a if  not set(i).isdisjoint(b)]
print('list of vowels:',c)
print('COMPLETE'.center(50,'='))

print('3]Accept string and separate the vowels contain word and consonants words')
a=input('Enter a string :').lower().split()
b=set('aeiou')
c=[i for i in a if  not set(i).isdisjoint(b)]
d=[i for i in a if set(i).isdisjoint(b)]
print('list of vowels:',c)
print('list of consonants:',d)
print('COMPLETE'.center(50,'='))

print('4]Accept string and separate the digits, alphabets,special symbal')
a=input('Enter a string :').lower().split()
b=[i for i in a if i.isalpha()]
c=[i for i in a if i.isdigit()]
d=[i for i in a if i not in b and i not in c]
D=[i for i in a if not i.isalpha() and not i.isdigit()]
print('alphabets:',b)
print('Digits:',c)
print('special symbal:',d)
print('special symbal:',D)
print('COMPLETE'.center(50,'='))




